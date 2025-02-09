from typing import Dict, Type

from model.filter_request import FilterType
from .filter_strategies import (
    EqualsFilter, ContainsFilter, GreaterThanFilter, LessThanFilter, RangeFilter, InFilter
)
from .base_filter import BaseFilter

FILTER_MAPPING: Dict[FilterType, Type[BaseFilter]] = {
    FilterType.EQUALS: EqualsFilter,
    FilterType.CONTAINS: ContainsFilter,
    FilterType.GREATER_THAN: GreaterThanFilter,
    FilterType.LESS_THAN: LessThanFilter,
    FilterType.RANGE: RangeFilter,
    FilterType.IN: InFilter,
}

def get_filter_strategy(filter_type: FilterType) -> Type[BaseFilter]:
    return FILTER_MAPPING.get(filter_type)
