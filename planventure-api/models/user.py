from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from utils.password_utils import hash_password, check_password as verify_password

# 延遲導入 db，避免循環導入
def get_db():
    from models import db
    return db

class User(get_db().Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    trips = relationship("Trip", back_populates="user")

    def set_password(self, password: str):
        self.password_hash = hash_password(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return verify_password(password, self.password_hash.encode('utf-8'))


