from flask import Blueprint, request, jsonify
from models import db, User
from utils.password_utils import hash_password
from utils.jwt_utils import create_access_token
import re

auth_bp = Blueprint('auth', __name__)

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    用戶註冊
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              format: email
              example: "user@example.com"
              description: 用戶電子郵件地址
            password:
              type: string
              format: password
              example: "password123"
              description: 用戶密碼
    responses:
      201:
        description: 用戶註冊成功
        schema:
          type: object
          properties:
            message:
              type: string
              example: "User registered successfully."
            token:
              type: string
              example: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
              description: JWT 訪問令牌
      400:
        description: 註冊失敗 - 無效輸入或郵箱已存在
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Email and password are required."
    """
    print("Register endpoint called")
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400
    if not re.match(EMAIL_REGEX, email):
        return jsonify({'error': 'Invalid email format.'}), 400
    
    # 檢查用戶是否已存在
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered.'}), 400
    
    # 創建新用戶
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    
    token = create_access_token({"user_id": user.id, "email": user.email})
    return jsonify({'message': 'User registered successfully.', 'token': token}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    用戶登入
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              format: email
              example: "user@example.com"
              description: 用戶電子郵件地址
            password:
              type: string
              format: password
              example: "password123"
              description: 用戶密碼
    responses:
      200:
        description: 登入成功
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Login successful."
            token:
              type: string
              example: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
              description: JWT 訪問令牌
            user:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                email:
                  type: string
                  example: "user@example.com"
      400:
        description: 登入失敗 - 缺少必要欄位
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Email and password are required."
      401:
        description: 登入失敗 - 認證錯誤
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Invalid email or password."
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400
    
    if not re.match(EMAIL_REGEX, email):
        return jsonify({'error': 'Invalid email format.'}), 400
    
    # 查找用戶
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid email or password.'}), 401
    
    token = create_access_token({"user_id": user.id, "email": user.email})
    return jsonify({
        'message': 'Login successful.',
        'token': token,
        'user': {
            'id': user.id,
            'email': user.email
        }
    }), 200
