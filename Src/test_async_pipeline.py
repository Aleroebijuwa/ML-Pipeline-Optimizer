import asyncio
import time
from async_pipeline import run_pipeline


if __name__ == "__main__":
    start = time.time()

    asyncio.run(run_pipeline())

    end = time.time()

    print(f"\nTOTAL PIPELINE TIME: {end - start:.2f} seconds") 
    