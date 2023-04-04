""" Shortest Word

Given a string of words, return the lenght of the shortest word(s)
"""


def find_short(s):
    words_length = [len(word) for word in s.split(sep=" ")]
    shortest_length = min(words_length)

    return shortest_length
