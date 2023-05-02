""" File Owners
https://www.testdome.com/questions/python/file-owners/94848

Expected Time: 10min

Implement a group_by_owners function that:
    Accepts a dictionary containing the file owner name for each file name.
    Returns a dictionary containing a list of file names for each owner name, in any order.

For example:
    for dictionary 
        {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
    the group_by_owners function should return 
        {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
"""


def group_by_owners(files):
    """
    This function takes a dictionary with the owners name for each file and returns a 
    dictionary containing a list of files for each owner

    Args:
        files (dict): Dictionary {owner: file} 
    Return:
        file_owners (dict): Dictionariy {owner: files[]} 
    """

    # Solution 1: For bucle
    file_owners = {}

    for name in files.values():
        file_owners[name] = [x for x in files if files[x] == name]

    # Sol 2: Diccionario por comprension
    # file_owners = {name: [file for file, owner in files.items() if owner == name] for name in set(files.values())}

    return file_owners


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }

    print(group_by_owners(files))
