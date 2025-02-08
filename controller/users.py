
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from db_conn.connection import get_db
from model.users import User as UserModel
from repository.users import UserRepository
from utility.logger.logger import logger

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserModel])
async def get_users(db: AsyncSession = Depends(get_db)):
    """API to fetch all users asynchronously."""
    try:
        users = await UserRepository.get_all_users(db)
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        return users
    except Exception as e:
        logger.error(f"Failed to fetch users: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
