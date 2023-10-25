"""
Given a non-empty array of integers, return the result of multiplying the values together in order. 

Example:
    [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24 
"""
import math 
import numpy as np
from functools import reduce

# 1st Method: Using a for bucle
def grow(arr):
    result = 1
    for a in arr:
        result *= a

    return result

# 2nd Method: Using numpy
def grow_with_numpy(arr):
    return np.prod(arr)


# 3rd Method: Using a lambda function and reduce
def grow_with_reduce(arr):
    return reduce((lambda x, y: x * y), arr)


# 4th Method: Using math module
def grow_with_math(arr):
    return math.prod(arr)

arr = [1, 2, 3, 4]
print(grow(arr))
print(grow_with_numpy(arr))
print(grow_with_reduce(arr))
print(grow_with_math(arr))
