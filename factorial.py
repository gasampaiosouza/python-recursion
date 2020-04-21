# from functools import lru_cache

# @lru_cache(maxsize = 1000) # not really necessary in this situation
def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


print( factorial(5) ) # 120