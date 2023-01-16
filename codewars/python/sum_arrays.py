"""
Write a function that takes an array of numbers and returns the sum of the numbers. 
- The numbers can be negative or non-integer. 
- If the array does not contain any numbers then you should return 0.
"""

def sum_array(a):
    # First solution
    # sum = 0
    # for number in a:
    #     sum += number
    # return sum
    
    # Second solution
    return sum(a)


array = []
print(sum_array(array))