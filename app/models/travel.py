from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, text
from app.db.database import Base

class TravelRecommendation(Base):
    __tablename__ = "travel_recommendations"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(100), nullable=False)
    days = Column(Integer, nullable=False)
    type = Column(String(20), nullable=False)
    recommendation = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('NOW()'))
    updated_at = Column(TIMESTAMP, server_default=text('NOW()'), onupdate=text('NOW()'))