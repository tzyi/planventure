from flask import Blueprint, jsonify
from utils.auth_middleware import auth_required

protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/protected', methods=['GET'])
@auth_required
def protected():
    return jsonify({'message': '這是一個受保護的路由，只有帶有有效 JWT 的用戶可以看到這個訊息。'})
