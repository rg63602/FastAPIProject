from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    status_code: int
    message: str
    data: Optional[List[T]] = None
    current_page : Optional[int] = None
    items_per_page: Optional[int] = None
    total_items: Optional[int] = None
    total_pages: Optional[int] = None


