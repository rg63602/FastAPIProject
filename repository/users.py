from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from schema.users import User as UserSchema
from model.users import User as UserModel
from utility.exception_handler.FastAPIExceptions.UsersException import UserNotFoundException
from utility.logger.logger import logger

class UserRepository:
    """Repository for User model handling async DB operations."""

    @staticmethod
    @logger.execution_timer
    async def get_all_users(session: AsyncSession, page: int = 1, items_per_page: int = 100):
        """Fetch all users asynchronously"""
        try:
            logger.info("Fetching all users from the database...")
            total_count = await session.scalar(select(func.count()).select_from(UserSchema))
            offset = (page - 1) * items_per_page
            result = await session.execute(select(UserSchema).offset(offset).limit(items_per_page))
            users = result.scalars().all()
            users_list = [UserModel(**user.__dict__) for user in users]
            return users_list, total_count
        except Exception as e:
            logger.error(f"Error fetching users: {str(e)}")
            raise e