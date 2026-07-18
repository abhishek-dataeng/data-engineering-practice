import json
import logging
import sys

logging.basicConfig(level=logging.INFO,handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)

class ConfigError(Exception):
    """Base exception class for config error"""
    pass

class ConfigNotFoundError(ConfigError):
    pass

class ConfigParseError(ConfigError):
    pass

class ConfigValidationError(ConfigError):
    pass

REQ_KEYS = ('db_host','db_port','db_name')

def load_and_validate_config(fpath:str) -> dict:
    try:
        with open(fpath,'r') as file:
            config = json.load(file)
    except FileNotFoundError as e:
        raise ConfigNotFoundError(f"Config file: {fpath} not found") from e
    except json.JSONDecodeError as e:
        raise ConfigParseError(f"Config file is not valid json") from e
    
    missing = [key for key in REQ_KEYS if key not in config]
    if missing:
        raise ConfigValidationError(f"Config missing required keys: {missing}")
    
    return config

def safe_startup(path: str):
    try:
        config = load_and_validate_config(path)
        logging.info("Config loaded success")
        return config
    except ConfigNotFoundError as e:
        logger.critical(f"Config file: {path} is missing")
        raise
    except ConfigParseError as e:
        logger.critical("Can not start config file is malformed")
        raise
    except ConfigValidationError as e:
        logger.critical(f"Can not start due to error:{e}")
        raise

# logger.info(load_and_validate_config('/home/abhishek/projects/python_prep/data/db_config1.json'))

logger.info(safe_startup('/home/abhishek/projects/python_prep/data/db_config.json'))