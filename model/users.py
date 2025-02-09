from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: UUID
    user_name: str
    email: str
    created_by: Optional[str] = None
    created_at: datetime
    updated_by: Optional[str] = None
    updated_at: datetime

class UserCreate(BaseModel):
    user_name: str
    email: str
    created_by: Optional[str] = None
    updated_by: Optional[str] = None

class UserUpdate(BaseModel):
    user_name: Optional[str] = None
    email: Optional[str] = None
    updated_by: Optional[str] = None
