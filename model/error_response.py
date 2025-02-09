import uuid
from typing import Optional

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Standardized error response."""
    status_code: int
    error_code: int
    message: str
    request_id: str = str(uuid.uuid4())
    details: Optional[str] = None
