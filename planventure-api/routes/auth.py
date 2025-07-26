from flask import Blueprint, request, jsonify
from models import db, User
from utils.password_utils import hash_password
from utils.jwt_utils import create_access_token
import re

auth_bp = Blueprint('auth', __name__)

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

@auth_bp.route('/register', methods=['POST'])
def register():
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
