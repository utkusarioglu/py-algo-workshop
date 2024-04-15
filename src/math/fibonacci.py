
def fibonacci(index: int, cache=[0, 1])-> int:
    """Fibonacci algo exploiting the optional variable instantiation 
    procedure in python
    """
    if index == len(cache):
        cache.append(fibonacci(index - 1) + fibonacci(index - 2))
    return cache[index]
