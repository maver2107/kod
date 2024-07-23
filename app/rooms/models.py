from sqlalchemy import JSON, Column, Computed, Date, ForeignKey, Integer, String
from app.database import Base


class Rooms(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=True)
    quantity = Column(Integer, nullable=False)
    image_id = Column(String)