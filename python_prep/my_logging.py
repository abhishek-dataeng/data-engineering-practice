import logging

logging.basicConfig(
    level=logging.CRITICAL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    # datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("/home/abhishek/projects/python_prep/logs/app_log1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.critical("This is a critical message.")
logger.debug("This is a debug message.")
logger.info("Logging is set up successfully.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")


#logging exception with full traceback
# try:
#     1 / 0
# except Exception as e:
#     logger.exception("An exception occurred: %s", e)

#rotating log files

from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("/home/abhishek/projects/python_prep/logs/app_log1.log", maxBytes=2000, backupCount=5 )
logger.addHandler(handler)