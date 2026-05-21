import numpy as np



def slow_square(data):

    result = []

    for x in data:
        result.append(x ** 2)

    return result



def fast_square(data):

    return np.square(data)



def batch_generator(data, batch_size):

    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]
