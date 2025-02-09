from pydantic import BaseModel, Field
from typing import Any, List, Optional
from enum import Enum

class FilterType(str, Enum):
    EQUALS = "equals"
    CONTAINS = "contains"
    GREATER_THAN = "greater_than"
    LESS_THAN = "less_than"
    RANGE = "range"
    IN = "in"

class ColumnType(str, Enum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    DATE = "date"

class Filter(BaseModel):
    column_name: str = Field(..., description="Database column to filter")
    column_type: ColumnType = Field(..., description="Type of column")
    filter_type: FilterType = Field(..., description="Type of filter operation")
    value: Any = Field(..., description="Filter value")
    extra_value: Optional[Any] = Field(None, description="Used for range filters")

class FilterRequest(BaseModel):
    filters: List[Filter] = Field(..., description="List of filters")
    page: int = Field(1, description="Page number for pagination")
    items_per_page: int = Field(10, description="Items per page")
