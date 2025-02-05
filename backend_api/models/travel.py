from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, text, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from db.database import Base

class TravelRecommendation(Base):
    __tablename__ = "travel_recommendations"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(100), nullable=False)
    days = Column(Integer, nullable=False)
    type = Column(String(20), nullable=False)
    recommendation = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('NOW()'))
    updated_at = Column(TIMESTAMP, server_default=text('NOW()'), onupdate=text('NOW()'))

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    country = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    timezone = Column(String(50), nullable=True)
    created_at = Column(TIMESTAMP, server_default=text('NOW()'))
    updated_at = Column(TIMESTAMP, server_default=text('NOW()'), onupdate=text('NOW()'))

    # Relationship with attractions
    attractions = relationship("Attraction", back_populates="city")

class Attraction(Base):
    __tablename__ = "attractions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    description = Column(Text)
    category = Column(String(50), nullable=True)  # e.g., museum, park, temple, etc.
    address = Column(String(500), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    visiting_hours = Column(JSON, nullable=True)  # Store opening hours in JSON format
    admission_fee = Column(JSON, nullable=True)   # Store different ticket types and prices
    recommended_duration = Column(Integer, nullable=True)  # in minutes
    created_at = Column(TIMESTAMP, server_default=text('NOW()'))
    updated_at = Column(TIMESTAMP, server_default=text('NOW()'), onupdate=text('NOW()'))

    # Relationship with city
    city = relationship("City", back_populates="attractions")