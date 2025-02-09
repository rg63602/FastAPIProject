from sqlalchemy.orm import Query
from abc import ABC, abstractmethod


class BaseFilter(ABC):
    """Abstract class to define a filter strategy."""

    @abstractmethod
    def apply(self, query: Query, column, value):
        pass
