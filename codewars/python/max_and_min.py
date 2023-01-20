"""
Make two functions that receive a list of integers as input and return the largest and lowest number in that list, respectively.
"""

def minimum(list):
    # Fisrt solution
    minimum = list[0]

    for number in list:
        if number < minimum: minimum = number

    return minimum

    # Second solution
    # return min(list)

def maximum(list):
    # First solution
    maximum = list[0]

    for number in list:
        if number > maximum: maximum = number

    return maximum

    # Second solution
    # return max(list)

list = [-52, 56, 30, 29, -54, 0, -110]

print(minimum(list))
print(maximum(list))
