from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from utils.password_utils import hash_password, verify_password

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    trips = relationship("Trip", back_populates="user")
    
    def set_password(self, password: str) -> None:
        """
        Set the user's password by hashing it.
        
        Args:
            password (str): The plain text password to set
        """
        self.password_hash = hash_password(password)
    
    def check_password(self, password: str) -> bool:
        """
        Check if the provided password matches the user's password.
        
        Args:
            password (str): The plain text password to verify
            
        Returns:
            bool: True if password matches, False otherwise
        """
        return verify_password(password, self.password_hash)
    
    def to_dict(self) -> dict:
        """
        Convert the user object to a dictionary (excluding sensitive data).
        
        Returns:
            dict: User data without password hash
        """
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __repr__(self) -> str:
        """
        String representation of the User object.
        
        Returns:
            str: User representation
        """
        return f"<User(id={self.id}, email='{self.email}')>"
