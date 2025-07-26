from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 在這裡導入所有模型以確保它們都被註冊
from .user import User
from .trip import Trip

__all__ = ['db', 'User', 'Trip']
