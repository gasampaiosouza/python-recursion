from functools import lru_cache

@lru_cache(maxsize = 1000) # cache value.
def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print( fibonacci(50) ) # 12586269025 || with 0 delay