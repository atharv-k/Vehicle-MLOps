import logging 
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
from from_root import from_root

#constants for log_configurations

LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
MAX_LOG_SIZE = 5*1024*1024 #5MB
BACKUP_COUNT = 3 #number of backup log files to keep

# COnstruct log file path

log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True) #create log directory if it doesn't exist
log_file_path = os.path.join(log_dir_path, LOG_FILE)

def configure_logger():
    """
    Configures the logger to write logs to a file with rotation and also to the console
    """

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    #file handler for rotating log files
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    #console handler for outputting logs to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    #add handlers to the logger

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

#Configure the logger when this module is imported

configure_logger()