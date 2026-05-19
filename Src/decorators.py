import time
import logging
from functools import wraps 

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
) 
def timer(func):
    

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        duration = end_time - start_time

        logging.info(f"[TIMER] {func.__name__} took {duration:.6f} seconds")

        return result

    return wrapper



def logger(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"[LOGGER] Calling {func.__name__}")
        logging.info(f"[LOGGER] args: {args}, kwargs: {kwargs}")

        result = func(*args, **kwargs)

        logging.info(f"[LOGGER] {func.__name__} returned {result}")

        return result

    return wrapper

