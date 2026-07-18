import logging
import json
import sys
import time

logging.basicConfig(level=logging.INFO,handlers=[logging.StreamHandler(sys.stdout)])

logger = logging.getLogger(__name__)

class PipelineError(Exception):
    """Base exception class for all pipeline related error"""
    pass

class DataValidationError(PipelineError):
    """Raised when input data validation has error"""
    pass

class FileFormatError(PipelineError):
    """Raised when incoming file format is wrong"""
    pass

def validate_row(order:dict):
    for row in order:
        if 'order_id' not in row:
            raise DataValidationError(f'{row} is missing amount field ')

# Exception chaining — preserving the original cause
def load_json(fpath: str) -> dict:
    try:
        with open(fpath,'r') as f:
            return json.load(f)
    except FileNotFoundError as e:
        # logger.info(f"Exception Occured: {e}") 
        raise PipelineError(f"Json File {fpath} not found") from e


# logger.info(load_json('/home/abhishek/projects/python_prep/data/test_json1.json'))

# projects/python_prep/data/test_json.json

# def fetch_fn():
#     pass

def fetch_with_retry(retrycnt:int = 3, sleeptime:float = 1.0):
    last_exception = None
    for i in range(1,retrycnt+1):
        try:
            logger.info("Success in try block in attempt %d/%d",i,retrycnt)
            #return "Return: try block completed"
        except (ConnectionError, TimeoutError,ZeroDivisionError) as e:
            last_exception = e
            logger.warning(f'Attemt %d/%d failed due to error %s',i,retrycnt,e)
            time.sleep(sleeptime)
        else:
            # if try block is passed else block is executed
            logger.info('Running else block after try block')
            return f"Return: Else block completed in attempt {i}"
        finally:
            # regarding of try or except block finally block is executed like db connection close
            logger.info("Executing finally block") 
    raise PipelineError(f'All {retrycnt} attempts are failed') from last_exception

logger.info(fetch_with_retry())        
