"""
    Exercise N° 9
    Given an integer x return true if x is a palindrome, and false otherwise
"""
# First solution
# def isPalindrome(x: int) -> bool:
#     original_number = str(x)
#     reversed_number = original_number[::-1]
    
#     return True if original_number == reversed_number else False


# Second solution
# - Negative numbers never could be palindromes
# - Numbers from 0 to 9 always be palindromes
def isPalindrome(x:int) -> bool:
    if x < 0: return False
    if x < 9: return True
    
    number = str(x)
    return True if number == number[::-1] else False

print(isPalindrome(121))
