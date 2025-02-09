from sqlalchemy.orm import Query
from .base_filter import BaseFilter

class EqualsFilter(BaseFilter):
    def apply(self, query: Query, column, value):
        return query.filter(column == value)

class ContainsFilter(BaseFilter):
    def apply(self, query: Query, column, value):
        return query.filter(column.ilike(f"%{value}%"))

class GreaterThanFilter(BaseFilter):
    def apply(self, query: Query, column, value):
        return query.filter(column > value)

class LessThanFilter(BaseFilter):
    def apply(self, query: Query, column, value):
        return query.filter(column < value)

class RangeFilter(BaseFilter):
    def apply(self, query: Query, column, value):
        return query.filter(column.between(value[0], value[1]))

class InFilter(BaseFilter):
    def apply(self, query: Query, column, value):
        return query.filter(column.in_(value))

class BooleanEqualsFilter(BaseFilter):
    def apply(self, query, column, value):
        return query.filter(column.is_(value))