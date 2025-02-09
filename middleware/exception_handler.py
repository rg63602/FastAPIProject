import traceback
import uuid
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

from config.messages import Message
from config.status_code import StatusCode
from utility.error_response import ErrorResponse
from utility.exception_handler.exception import CustomException
from utility.logger.logger import logger


class ExceptionHandler:
    """Handles custom and generic exceptions globally."""

    @staticmethod
    async def custom_exception_handler(request: Request, exc: CustomException):
        """Handles all custom exceptions."""
        request_id = str(uuid.uuid4())
        error_response = ErrorResponse(
            status_code=exc.status_code,
            message=exc.message,
            request_id=request_id,
            details=str(exc.details)
        )
        logger.error(f"CustomException: {exc.message} | Request ID: {request_id} | Details: {exc.details}")
        return JSONResponse(status_code=exc.status_code, content=error_response.model_dump())

    @staticmethod
    async def generic_exception_handler(request: Request, exc: Exception):
        """Handles all uncaught exceptions."""
        request_id = str(uuid.uuid4())
        error_trace = traceback.format_exc()

        error_response = ErrorResponse(
            status_code=StatusCode.SERVER_ERROR,
            message=Message.INTERNAL_ERROR,
            request_id=request_id,
            details=str(exc)  # Optionally log full trace for debugging
        )

        logger.error(f"Unhandled Exception: {str(exc)} | Request ID: {request_id}\n{error_trace}")
        return JSONResponse(status_code=StatusCode.SERVER_ERROR, content=error_response.model_dump())


def add_exception_handlers(app: FastAPI):
    """Attach exception handlers to FastAPI app."""
    app.add_exception_handler(CustomException, ExceptionHandler.custom_exception_handler)
    app.add_exception_handler(Exception, ExceptionHandler.generic_exception_handler)
