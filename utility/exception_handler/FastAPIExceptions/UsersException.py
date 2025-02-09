from config.messages import Message
from config.status_code import StatusCode
from utility.exception_handler.exception import CustomException


class UserNotFoundException(CustomException):
    """Raised when a user is not found in the database."""
    def __init__(self, detail: str = None):
        super().__init__(
            status_code=StatusCode.BAD_REQUEST,
            error_code=StatusCode.USER_NOT_FOUND,
            message=Message.USER_NOT_FOUND,
            details=detail
        )
class UserAlreadyExistsException(CustomException):
    """Raised when a user already exists in the database."""
    def __init__(self):
        super().__init__(
            status_code=StatusCode.BAD_REQUEST,
            error_code=StatusCode.USER_ALREADY_EXISTS,
            message=Message.ERROR,
            details=Message.USER_ALREADY_EXISTS,
        )