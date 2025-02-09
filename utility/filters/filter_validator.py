from typing import Dict, Set
from model.filter_request import FilterType, ColumnType
from utility.exception_handler.FastAPIExceptions.filter_exceptions import InvalidFilterColumnType
from utility.logger.logger import logger


# Define valid filter-type-to-column-type mapping
FILTER_VALIDATION_RULES: Dict[FilterType, Set[ColumnType]] = {
    FilterType.EQUALS: {ColumnType.STRING, ColumnType.NUMBER, ColumnType.DATE, ColumnType.BOOLEAN},
    FilterType.CONTAINS: {ColumnType.STRING},
    FilterType.GREATER_THAN: {ColumnType.NUMBER, ColumnType.DATE},
    FilterType.LESS_THAN: {ColumnType.NUMBER, ColumnType.DATE},
    FilterType.RANGE: {ColumnType.NUMBER, ColumnType.DATE},
    FilterType.IN: {ColumnType.STRING, ColumnType.NUMBER, ColumnType.DATE, ColumnType.BOOLEAN},
    FilterType.BOOLEAN_EQUALS: {ColumnType.BOOLEAN},
}


def validate_filter_type(filter_obj):
    """
    Ensures the filter type is compatible with the column type.

    Raises:
        InvalidFilterValueError: If the filter type is invalid for the given column.
    """
    allowed_types = FILTER_VALIDATION_RULES.get(filter_obj.filter_type, set())

    if filter_obj.column_type not in allowed_types:
        logger.error(f'InvalidFilterValueError - {filter_obj.column_name} - {filter_obj.column_type} - {list(allowed_types)}')
        raise InvalidFilterColumnType()
