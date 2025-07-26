from flask import Blueprint, request, jsonify, g
from models import db, Trip, User
from utils.auth_middleware import auth_required
from utils.jwt_utils import verify_access_token
from datetime import datetime
import json

trip_bp = Blueprint('trip', __name__)

def get_current_user():
    """從 JWT token 中獲取當前用戶"""
    auth_header = request.headers.get('Authorization', None)
    if not auth_header or not auth_header.startswith('Bearer '):
        return None
    
    token = auth_header.split(' ')[1]
    payload = verify_access_token(token)
    if not payload:
        return None
    
    user = User.query.get(payload['user_id'])
    return user

@trip_bp.route('/trips', methods=['POST'])
@auth_required
def create_trip():
    """
    創建新行程
    ---
    tags:
      - Trips
    security:
      - Bearer: []
    parameters:
      - in: body
        name: trip
        description: 行程資料
        required: true
        schema:
          type: object
          required:
            - destination
            - start_date
            - end_date
          properties:
            destination:
              type: string
              description: 目的地
              example: "東京"
            start_date:
              type: string
              format: date
              description: 開始日期 (YYYY-MM-DD)
              example: "2024-03-01"
            end_date:
              type: string
              format: date
              description: 結束日期 (YYYY-MM-DD)
              example: "2024-03-07"
            coordinates:
              type: object
              description: 座標資訊
              properties:
                lat:
                  type: number
                  example: 35.6762
                lng:
                  type: number
                  example: 139.6503
            itinerary:
              type: array
              description: 行程規劃
              items:
                type: object
                properties:
                  day:
                    type: integer
                    example: 1
                  plan:
                    type: string
                    example: "參觀淺草寺"
    responses:
      201:
        description: 行程創建成功
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Trip created successfully"
            trip:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                destination:
                  type: string
                  example: "東京"
                start_date:
                  type: string
                  example: "2024-03-01"
                end_date:
                  type: string
                  example: "2024-03-07"
      400:
        description: 請求資料錯誤
      401:
        description: 未授權
    """
    try:
        user = get_current_user()
        if not user:
            return jsonify({'msg': 'User not found'}), 401

        data = request.get_json()
        if not data:
            return jsonify({'msg': 'No data provided'}), 400

        # 驗證必填欄位
        required_fields = ['destination', 'start_date', 'end_date']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'msg': f'Missing required field: {field}'}), 400

        # 驗證日期格式
        try:
            start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'msg': 'Invalid date format. Use YYYY-MM-DD'}), 400

        # 驗證日期邏輯
        if start_date >= end_date:
            return jsonify({'msg': 'End date must be after start date'}), 400

        # 創建新行程
        trip = Trip(
            user_id=user.id,
            destination=data['destination'],
            start_date=start_date,
            end_date=end_date,
            coordinates=data.get('coordinates'),
            itinerary=data.get('itinerary')
        )

        db.session.add(trip)
        db.session.commit()

        return jsonify({
            'message': 'Trip created successfully',
            'trip': {
                'id': trip.id,
                'destination': trip.destination,
                'start_date': trip.start_date.isoformat(),
                'end_date': trip.end_date.isoformat(),
                'coordinates': trip.coordinates,
                'itinerary': trip.itinerary
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': f'Error creating trip: {str(e)}'}), 500

@trip_bp.route('/trips', methods=['GET'])
@auth_required
def get_user_trips():
    """
    獲取用戶的所有行程
    ---
    tags:
      - Trips
    security:
      - Bearer: []
    responses:
      200:
        description: 成功獲取行程列表
        schema:
          type: object
          properties:
            trips:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  destination:
                    type: string
                    example: "東京"
                  start_date:
                    type: string
                    example: "2024-03-01"
                  end_date:
                    type: string
                    example: "2024-03-07"
                  coordinates:
                    type: object
                  itinerary:
                    type: array
      401:
        description: 未授權
    """
    try:
        user = get_current_user()
        if not user:
            return jsonify({'msg': 'User not found'}), 401

        trips = Trip.query.filter_by(user_id=user.id).all()
        
        trips_data = []
        for trip in trips:
            trips_data.append({
                'id': trip.id,
                'destination': trip.destination,
                'start_date': trip.start_date.isoformat(),
                'end_date': trip.end_date.isoformat(),
                'coordinates': trip.coordinates,
                'itinerary': trip.itinerary
            })

        return jsonify({'trips': trips_data}), 200

    except Exception as e:
        return jsonify({'msg': f'Error fetching trips: {str(e)}'}), 500

@trip_bp.route('/trips/<int:trip_id>', methods=['GET'])
@auth_required
def get_trip(trip_id):
    """
    獲取特定行程詳情
    ---
    tags:
      - Trips
    security:
      - Bearer: []
    parameters:
      - in: path
        name: trip_id
        type: integer
        required: true
        description: 行程 ID
    responses:
      200:
        description: 成功獲取行程詳情
        schema:
          type: object
          properties:
            trip:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                destination:
                  type: string
                  example: "東京"
                start_date:
                  type: string
                  example: "2024-03-01"
                end_date:
                  type: string
                  example: "2024-03-07"
                coordinates:
                  type: object
                itinerary:
                  type: array
      401:
        description: 未授權
      404:
        description: 行程不存在
    """
    try:
        user = get_current_user()
        if not user:
            return jsonify({'msg': 'User not found'}), 401

        trip = Trip.query.filter_by(id=trip_id, user_id=user.id).first()
        if not trip:
            return jsonify({'msg': 'Trip not found'}), 404

        trip_data = {
            'id': trip.id,
            'destination': trip.destination,
            'start_date': trip.start_date.isoformat(),
            'end_date': trip.end_date.isoformat(),
            'coordinates': trip.coordinates,
            'itinerary': trip.itinerary
        }

        return jsonify({'trip': trip_data}), 200

    except Exception as e:
        return jsonify({'msg': f'Error fetching trip: {str(e)}'}), 500

@trip_bp.route('/trips/<int:trip_id>', methods=['PUT'])
@auth_required
def update_trip(trip_id):
    """
    更新行程
    ---
    tags:
      - Trips
    security:
      - Bearer: []
    parameters:
      - in: path
        name: trip_id
        type: integer
        required: true
        description: 行程 ID
      - in: body
        name: trip
        description: 更新的行程資料
        required: true
        schema:
          type: object
          properties:
            destination:
              type: string
              description: 目的地
              example: "大阪"
            start_date:
              type: string
              format: date
              description: 開始日期 (YYYY-MM-DD)
              example: "2024-03-01"
            end_date:
              type: string
              format: date
              description: 結束日期 (YYYY-MM-DD)
              example: "2024-03-07"
            coordinates:
              type: object
              description: 座標資訊
            itinerary:
              type: array
              description: 行程規劃
    responses:
      200:
        description: 行程更新成功
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Trip updated successfully"
            trip:
              type: object
      400:
        description: 請求資料錯誤
      401:
        description: 未授權
      404:
        description: 行程不存在
    """
    try:
        user = get_current_user()
        if not user:
            return jsonify({'msg': 'User not found'}), 401

        trip = Trip.query.filter_by(id=trip_id, user_id=user.id).first()
        if not trip:
            return jsonify({'msg': 'Trip not found'}), 404

        data = request.get_json()
        if not data:
            return jsonify({'msg': 'No data provided'}), 400

        # 更新目的地
        if 'destination' in data:
            trip.destination = data['destination']

        # 更新日期
        if 'start_date' in data:
            try:
                trip.start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'msg': 'Invalid start_date format. Use YYYY-MM-DD'}), 400

        if 'end_date' in data:
            try:
                trip.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'msg': 'Invalid end_date format. Use YYYY-MM-DD'}), 400

        # 驗證日期邏輯
        if trip.start_date >= trip.end_date:
            return jsonify({'msg': 'End date must be after start date'}), 400

        # 更新座標和行程
        if 'coordinates' in data:
            trip.coordinates = data['coordinates']

        if 'itinerary' in data:
            trip.itinerary = data['itinerary']

        db.session.commit()

        trip_data = {
            'id': trip.id,
            'destination': trip.destination,
            'start_date': trip.start_date.isoformat(),
            'end_date': trip.end_date.isoformat(),
            'coordinates': trip.coordinates,
            'itinerary': trip.itinerary
        }

        return jsonify({
            'message': 'Trip updated successfully',
            'trip': trip_data
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': f'Error updating trip: {str(e)}'}), 500

@trip_bp.route('/trips/<int:trip_id>', methods=['DELETE'])
@auth_required
def delete_trip(trip_id):
    """
    刪除行程
    ---
    tags:
      - Trips
    security:
      - Bearer: []
    parameters:
      - in: path
        name: trip_id
        type: integer
        required: true
        description: 行程 ID
    responses:
      200:
        description: 行程刪除成功
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Trip deleted successfully"
      401:
        description: 未授權
      404:
        description: 行程不存在
    """
    try:
        user = get_current_user()
        if not user:
            return jsonify({'msg': 'User not found'}), 401

        trip = Trip.query.filter_by(id=trip_id, user_id=user.id).first()
        if not trip:
            return jsonify({'msg': 'Trip not found'}), 404

        db.session.delete(trip)
        db.session.commit()

        return jsonify({'message': 'Trip deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': f'Error deleting trip: {str(e)}'}), 500