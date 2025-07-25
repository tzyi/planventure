from sqlalchemy import Column, Integer, String, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .user import Base  # 修改這行

class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    destination = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    coordinates = Column(JSON, nullable=True)  # 例如: {"lat": ..., "lng": ...}
    itinerary = Column(JSON, nullable=True)    # 例如: [{"day": 1, "plan": ...}, ...]

    user = relationship("User", back_populates="trips")