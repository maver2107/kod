from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.bookings.models import Bookings


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings():
    async with async_session_maker() as session:
        query = select(Bookings)  #это значит SELECT * FROM bookings(так же как и в sql)
        result = await session.execute(query)  #await используется для ассинхронных функций(означает, что бы использовать запросс query)
        return result.mappings().all() #писать только так где используется конструкция result.all и result.scalars.all