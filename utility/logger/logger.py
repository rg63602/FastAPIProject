import logging
import os
import datetime
from config.config import LOGS_DIR  # Import log directory path from config
from config.constants import APP_ENV, APP_VERSION  # Import constants

# Generate log file name based on current date and time
log_filename = datetime.datetime.now().strftime("logs_%d_%m_%Y.txt")
log_filepath = os.path.join(LOGS_DIR, log_filename)

# Create logs directory if it doesn't exist
os.makedirs(LOGS_DIR, exist_ok=True)

# Create a logger
logger = logging.getLogger("FastAPI_App")
logger.setLevel(logging.INFO)

# File handler (creates a new log file for each run)
file_handler = logging.FileHandler(log_filepath, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Console handler (shows logs in terminal)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Updated Log Format: "INFO - local - version - datetime - message"
log_format = logging.Formatter(
    "%(levelname)s - %(env)s - v%(version)s - %(asctime)s - %(message)s"
)

# Custom log filter to inject environment and version
class CustomLogFilter(logging.Filter):
    def filter(self, record):
        record.env = APP_ENV  # Set environment (e.g., local, development, production)
        record.version = APP_VERSION  # Set app version
        return True

# Apply custom log filter
logger.addFilter(CustomLogFilter())

# Set formatter for handlers
file_handler.setFormatter(log_format)
console_handler.setFormatter(log_format)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
