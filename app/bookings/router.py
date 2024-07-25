from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.bookings.shemas import SBooking




router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingDAO.find_all()