import time
import numpy as np

from optimization import slow_square, fast_square
from profiler import profile_function


data = np.random.randint(1, 1000, size=1_000_000)


start = time.time()

profile_function(slow_square, data)

end = time.time()

print(f"\n Slow Version Time: {end - start:.4f} seconds")


start = time.time()

profile_function(fast_square, data)

end = time.time()

print(f"\n Optimized Version Time: {end - start:.4f} seconds")