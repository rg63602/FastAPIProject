from uuid import UUID

from sqlalchemy import func, text
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
            if users:
                raise UserNotFoundException(
                    detail="no users found, please try again later",
                )
            users_list = [UserModel(**user.__dict__) for user in users]
            return users_list, total_count
        except Exception as e:
            logger.error(f"Error fetching users: {str(e)}")
            raise e

    @staticmethod
    @logger.execution_timer
    async def get_user_by_id(session: AsyncSession, user_id: UUID):
        """Fetch a user by ID asynchronously"""
        try:
            query = select(UserSchema).where(UserSchema.id == user_id)
            user = await session.execute(query)
            user = user.scalars().all()
            if not user:
                raise UserNotFoundException()
            return [UserModel(**user.__dict__) for user in user]
        except Exception as e:
            logger.error(f"Error fetching user: {str(e)}")
            raise e

