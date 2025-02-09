from sqlalchemy.orm import Query
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import List, Type
from model.filter_request import Filter
from utility.exception_handler.FastAPIExceptions.filter_exceptions import InvalidFilterColumnError
from utility.filters.filter_factory import get_filter_strategy
from utility.filters.filter_validator import validate_filter_type
from utility.logger.logger import logger

def apply_filters(query: Query, model: Type[DeclarativeMeta], filters: List[Filter]) -> Query:
    """
    Applies multiple filters dynamically to a SQLAlchemy query.

    Args:
        query (Query): The SQLAlchemy query object.
        model (Type[DeclarativeMeta]): The SQLAlchemy model to filter.
        filters (List[Filter]): List of filter conditions.

    Returns:
        Query: Modified query with applied filters.
    """
    try:
        for filter_obj in filters:
            column = getattr(model, filter_obj.column_name, None)
            if not column:
                raise InvalidFilterColumnError()

            # Validate filter type
            validate_filter_type(filter_obj)

            # Apply filter dynamically
            filter_class = get_filter_strategy(filter_obj.filter_type)
            query = filter_class().apply(query, column, filter_obj.value)

        return query

    except Exception as e:
        logger.error(f"Error applying filters: {e}")
        raise e
