import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Logs directory (all logs will be stored here)
LOGS_DIR = os.path.join(BASE_DIR, "utility", "logger", "logs")

# Ensure the log directory exists
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)







