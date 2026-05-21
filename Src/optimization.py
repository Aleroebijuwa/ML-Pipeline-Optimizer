import numpy as np

def fast_square(data):
    return np.square(data) 

def batch_generator(data, batch_size):
    """
    Yields batches instead of loading everything at once.
    """

    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size] 
 
