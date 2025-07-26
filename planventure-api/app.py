
from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
import os
from models import db  # 導入我們的 db 實例
from routes.auth import auth_bp
from routes.protected import protected_bp
from config.swagger_config import SWAGGER_CONFIG, SWAGGER_TEMPLATE
from config.cors_config import get_cors_config

app = Flask(__name__)

# CORS 配置 - 針對 React 前端優化
CORS(app, **get_cors_config())

# 初始化 Swagger
swagger = Swagger(app, config=SWAGGER_CONFIG, template=SWAGGER_TEMPLATE)

# 基本 SQLAlchemy 設定
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'planventure.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', f'sqlite:///{db_path}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 db 與 app
db.init_app(app)

# 導入模型以確保它們被註冊
from models import User, Trip

# Blueprints
from routes.trip import trip_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(protected_bp)
app.register_blueprint(trip_bp, url_prefix='/api')

@app.route('/')
def home():
    """
    歡迎頁面
    ---
    tags:
      - General
    responses:
      200:
        description: 歡迎訊息
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Welcome to PlanVenture API"
    """
    return jsonify({"message": "Welcome to PlanVenture API"})

@app.route('/health')
def health_check():
    """
    健康檢查端點
    ---
    tags:
      - General
    responses:
      200:
        description: 應用程式健康狀態
        schema:
          type: object
          properties:
            status:
              type: string
              example: "healthy"
    """
    return jsonify({"status": "healthy"})

@app.route('/cors-test')
def cors_test():
    """
    CORS 配置測試端點
    ---
    tags:
      - General
    responses:
      200:
        description: CORS 配置測試回應
        schema:
          type: object
          properties:
            message:
              type: string
              example: "CORS is working correctly"
            cors_enabled:
              type: boolean
              example: true
    """
    return jsonify({
        "message": "CORS is working correctly",
        "cors_enabled": True,
        "timestamp": "2025-07-26"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)