
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from config.messages import Message
from config.status_code import StatusCode
from db_conn.connection import get_db
from model.users import User as UserModel
from repository.users import UserRepository
from utility.exception_handler.FastAPIExceptions.UsersException import UserNotFoundException
from utility.exception_handler.exception import CustomException
from utility.logger.logger import logger
from utility.paginated_response import PaginatedResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=None)
@logger.execution_timer
async def get_users(db: AsyncSession = Depends(get_db),
                    page: int = Query(1, alias="page", ge=1),
                    items_per_page: int = Query(3, alias="per_page", ge=1, le=100)
                    ):
    """API to fetch all users asynchronously."""
    try:
        users, total_count = await UserRepository.get_all_users(db, page=page, items_per_page=items_per_page)
        total_pages = total_count // items_per_page
        if total_count % items_per_page != 0:
            total_pages += 1

        return PaginatedResponse[UserModel](
            status_code=StatusCode.SUCCESS,
            message=Message.SUCCESS,
            total_items=total_count,
            current_page=page,
            items_per_page=items_per_page,
            total_pages=total_pages,
            data=users
        ).model_dump()

    except CustomException as ce:
        raise ce
        logger.error(f"Custom Exception: {ce.message} | Details: {ce.details}")

    except Exception as e:
        logger.error(f"Failed to fetch users: {str(e)}")
        raise e
