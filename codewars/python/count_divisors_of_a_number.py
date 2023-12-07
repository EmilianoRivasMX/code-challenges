"""
    Count the number of divisors of a positive integer n.
"""
import math

# Solution 1: Traditional
# def count_divisors(number: int) -> int:
#     divisors_count = 1 # Because every number is divisor of itself  

#     for n in range(1, number):
#         if (number % n) == 0:
#             divisors_count += 1
#         else: continue
    
#     return divisors_count

# Solution 2:  Using square root to reduce the number of iterations
def count_divisors(number: int) -> int:
    divisors_count = 0  # Initialize to 0

    # Iterate up to the square root of the number
    for n in range(1, int(math.sqrt(number)) + 1):
        if number % n == 0:
            # If n is a divisor, increment count
            divisors_count += 1
            # If n is not the square root, count the corresponding divisor
            if n != number // n:
                divisors_count += 1

    return divisors_count


if __name__ == '__main__':
    number = int(input("Enter a number to count its divisors: "))
    divisors = count_divisors(number)
    print(divisors)
