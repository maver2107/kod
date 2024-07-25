from app.database import async_session_maker

from sqlalchemy import select

class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id) 
            result = await session.execute(query)
            return result.mappings().one_or_none()
            
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:    
            query = select(cls.model).filter_by(**filter_by) 
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:    
            query = select(cls.model).filter_by(**filter_by) #это значит SELECT * FROM bookings(так же как и в sql)
            result = await session.execute(query) #await используется для ассинхронных функций(означает, что бы использовать запросс query)
            return result.mappings().all() #писать только так где используется конструкция result.all и result.scalars.all
