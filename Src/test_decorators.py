from decorators import timer, logger


@timer
def slow_function(n):
    total = 0
    for i in range(n):
        total += i
    return total


@logger
def add(a, b):
    return a + b


if __name__ == "__main__":
    print("Testing logger:")
    add(5, 10)

    print("\nTesting timer:")
    slow_function(1000000)