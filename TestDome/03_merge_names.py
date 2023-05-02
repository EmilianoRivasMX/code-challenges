"""
https://www.testdome.com/questions/python/merge-names/94855

Expected Time: 10 min

Implement the unique_names method. When passed two arrays of names, it will return an array
containing the names that appear in either or both arrays. 
 
The returned array should have no duplicates.

For example:
    calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])

    should return an array containing Ava, Emma, Olivia, and Sophia in any order.
"""

# Solution 1
def unique_names(names1, names2):
    """
    This method returns an array containing the names that appear in either or both arrays

    Args:  
        names1 (list): List of names
        names2 (list): List of names

    Returns:
        unique_list (list): List of names that appear in either or both arrays
    """
    unique_set = set(names1).union(set(names2))
    unique_list = list(unique_set)
    return unique_list

# Solution 2
# def unique_names(names1, names2):
#     names = names1

#     for name in names2:
#         if name not in names:
#             names.append(name)

#     return names


if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]

    print(unique_names(names1, names2))
