"""Friend or Foe?

Make a program that filters a list of strings and returns a list with only your friends name in it.
"""

def friend(names):
    return [n for n in names if len(n) == 4]

# Test Cases    
print(friend(["Ryan", "Kieran", "Mark"]))
