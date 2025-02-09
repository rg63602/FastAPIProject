from fastapi import HTTPException


class CustomException(HTTPException):
    """Base class for all custom exceptions."""

    def __init__(self, status_code: int, message: str, details: str = None):
        super().__init__(status_code=status_code, detail={"message": message, "details": details})
        self.status_code = status_code
        self.message = message
        self.details = details

