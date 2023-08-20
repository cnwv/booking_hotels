from app.database import Base
from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DATE, Computed


class Bookings(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey("rooms.id"))
    user_id = Column(ForeignKey("users.id"))
    date_from = Column(DATE, nullable=False)
    date_to = Column(DATE, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed("(date_to - date_from) *  price"))
    total_days = Column(Integer, Computed("date_to - date_from"))
