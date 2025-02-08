from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from schema.users import User as UserSchema
from model.users import User as UserModel
from utility.logger.logger import logger

class UserRepository:
    """Repository for User model handling async DB operations."""

    @staticmethod
    async def get_all_users(session: AsyncSession):
        """Fetch all users asynchronously"""
        try:
            logger.info("Fetching all users from the database...")
            result = await session.execute(select(UserSchema))
            users = result.scalars().all()
            users_list = [UserModel(**user.__dict__) for user in users]
            return users_list
        except Exception as e:
            logger.error(f"Error fetching users: {str(e)}")
            raise