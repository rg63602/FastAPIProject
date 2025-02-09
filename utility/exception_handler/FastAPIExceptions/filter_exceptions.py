from config.messages import Message
from config.status_code import StatusCode
from utility.exception_handler.exception import CustomException


class InvalidFilterColumnError(CustomException):
    """Raised when invalid filter column is provided."""
    def __init__(self):
        super().__init__(
            status_code=StatusCode.BAD_REQUEST,
            error_code=StatusCode.INVALID_FILTER_COLUMN,
            message=Message.ERROR,
            details=Message.INVALID_FILTER_COLUMN
        )

class InvalidFilterColumnType(CustomException):
    """Raised when invalid filter type is provided."""
    def __init__(self):
        super().__init__(
            status_code=StatusCode.BAD_REQUEST,
            error_code=StatusCode.INVALID_FILTER_COLUMN_TYPE,
            message=Message.ERROR,
            details=Message.INVALID_FILTER_COLUMN_TYPE
        )

class InvalidFilterColumnValue(CustomException):
    """Raised when invalid filter value is provided."""
    def __init__(self):
        super().__init__(
            status_code=StatusCode.BAD_REQUEST,
            error_code=StatusCode.INVALID_FILTER_COLUMN_VALUE,
            message=Message.ERROR,
            details=Message.INVALID_FILTER_COLUMN
        )