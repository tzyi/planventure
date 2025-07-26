
from flask import Flask, jsonify
from flask_cors import CORS
import os
from models import db  # 導入我們的 db 實例
from routes.auth import auth_bp

app = Flask(__name__)
CORS(app)

# 基本 SQLAlchemy 設定
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'planventure.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', f'sqlite:///{db_path}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 db 與 app
db.init_app(app)

# 導入模型以確保它們被註冊
from models import User, Trip

# Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def home():
    return jsonify({"message": "Welcome to PlanVenture API"})

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True)