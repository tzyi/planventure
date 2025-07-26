from flask import request, jsonify
from functools import wraps
from utils.jwt_utils import verify_access_token

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'msg': 'Missing or invalid Authorization header'}), 401
        token = auth_header.split(' ')[1]
        payload = verify_access_token(token)
        if not payload:
            return jsonify({'msg': 'Invalid or expired token'}), 401
        # 可選: 將 payload 存入 g 物件供後續使用
        # from flask import g
        # g.user = payload
        return f(*args, **kwargs)
    return decorated_function
