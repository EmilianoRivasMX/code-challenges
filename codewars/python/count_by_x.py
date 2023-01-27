"""
Create a funtion with two arguments that will return an aray of the first n multiples of x
"""

def count_by(x, n):
    multiples = [x*n for n in range(1, n+1)]
    return multiples    


x = int(input())
n = int(input())

print(count_by(x, n))