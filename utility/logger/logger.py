import logging
import os
import datetime
import time
from functools import wraps
from contextvars import ContextVar
from config.config import LOGS_DIR  # Log directory path
from config.constants import APP_ENV, APP_VERSION, APP_NAME  # App Constants

# 🔹 Generate log file with current date
log_filename = datetime.datetime.now().strftime("logs_%d_%m_%Y.txt")
log_filepath = os.path.join(LOGS_DIR, log_filename)

# 🔹 Create logs directory if it doesn't exist
os.makedirs(LOGS_DIR, exist_ok=True)

class AppLogger:
    """Singleton Logger with Execution Time Tracking"""

    _instance = None  # Singleton instance
    execution_stack: ContextVar[list] = ContextVar("execution_stack", default=[])

    def __new__(cls):
        """Singleton Pattern - Ensures only one instance exists"""
        if cls._instance is None:
            cls._instance = super(AppLogger, cls).__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self):
        """Initialize Logger with Console & File Handlers"""
        self.logger = logging.getLogger(APP_NAME)
        self.logger.setLevel(logging.INFO)

        # 🔹 File Handler (Logs to File)
        file_handler = logging.FileHandler(log_filepath, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        # 🔹 Console Handler (Logs to Terminal)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # 🔹 Log Format
        log_format = logging.Formatter(
            "%(levelname)s - %(env)s - v%(version)s - %(asctime)s - %(message)s"
        )

        # 🔹 Custom Log Filter to Inject Metadata
        class CustomLogFilter(logging.Filter):
            def filter(self, record):
                record.env = APP_ENV  # Environment (local, production, etc.)
                record.version = APP_VERSION  # App version
                return True

        self.logger.addFilter(CustomLogFilter())

        # 🔹 Apply Format to Handlers
        file_handler.setFormatter(log_format)
        console_handler.setFormatter(log_format)

        # 🔹 Add Handlers to Logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message: str):
        """Logs INFO level messages"""
        self.logger.info(message)

    def error(self, message: str):
        """Logs ERROR level messages"""
        self.logger.error(message)

    def debug(self, message: str):
        """Logs ERROR level messages"""
        self.logger.debug(message)

    def log_execution_time(self, func_name, elapsed_time):
        """Logs execution time in hh:mm:ss.ms format"""
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = (seconds - int(seconds)) * 1000
        formatted_time = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{int(milliseconds):03}"

        indent = " -> ".join(self.execution_stack.get())  # Trace Nested Calls
        trace_path = f"{indent} -> {func_name}" if indent else func_name
        self.logger.info(f"Execution Time - {trace_path}: {formatted_time}")

    def execution_timer(self, func):
        """Decorator to log execution time for Sync & Async functions"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            stack = self.execution_stack.get()
            stack.append(func.__name__)
            start_time = time.perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                elapsed_time = time.perf_counter() - start_time
                self.log_execution_time(func.__name__, elapsed_time)
                stack.pop()

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            stack = self.execution_stack.get()
            stack.append(func.__name__)
            start_time = time.perf_counter()
            try:
                return await func(*args, **kwargs)
            finally:
                elapsed_time = time.perf_counter() - start_time
                self.log_execution_time(func.__name__, elapsed_time)
                stack.pop()

        return async_wrapper if hasattr(func, "__code__") and func.__code__.co_flags & 0x80 else wrapper

# 🔹 Instantiate Logger (Singleton)
logger = AppLogger()
