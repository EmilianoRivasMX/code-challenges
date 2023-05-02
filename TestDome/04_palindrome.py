"""
https://www.testdome.com/questions/python/palindrome/7962

Expected Time: 10 min

A palindrome is a word that reads the same backward or forward.
Write a function that checks if a given word is a palindrome (Character case should be ignored)

For example:
    is_palindrome("Deleveled") should return True as character case
    should be ignored, resulting in "deleveled", which is a palindrome since it 
    reads the same backward and forward.
"""


def is_palindrome(word):
    """
    This function checks if a given word is a palindrome (Character case should be ignored)

    Args:
        word (str): Word to check

    Returns:
        bool: True if the word is a palindrome, False otherwise
    """
    clear_word = word.lower().strip().replace(" ", "")
    reversed_word = clear_word[::-1]

    return clear_word == reversed_word


print(is_palindrome('Deleveled'))
print(is_palindrome('No palindromo'))
print(is_palindrome('Anita Lava la Tina'))
print(is_palindrome('Pepe Pecas'))
print(is_palindrome('Oiras orar a Rosario'))
