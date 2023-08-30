from generator.generator import first_n
from time import time


def duration(func):
    def wrapper(*args):
        start = time()
        response = func(*args)
        end = time()
        print(f"{func.__name__} took {end - start}")
        return response

    return wrapper


@duration
def decorated():
    return sum(first_n(10000000))
