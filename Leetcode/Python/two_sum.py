""" twoSum

Write a function that takes an array of integers nums and an integer target and returns 
the indices of the two numbers such that they add up to target.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    This function takes an array of integers 'nums' and an integer 'target' and looks for 
    the indices of the two numbers such that they add up to target.

    Args:
        nums (list[int]): List of integers
        target (int): Target number
    Return: Return indices of the two numbers such that they add up to target.
    """
    add_indexes = []

    # Sol 1: Comparing the addition of each element with the target
    # nums_len = len(nums)

    # for i in range(nums_len):
    #     for j in range(1, nums_len):
    #         print(f"{nums[i]} + {nums[j]} = {nums[i] + nums[j]}")
    #         if (i != j) and ((nums[i] + nums[j]) == target):
    #             add_indexes.append(i)
    #             add_indexes.append(j)
    #     if add_indexes:
    #         break

    # Sol 2: Using a hashmap
    nums_map = {}  # key: number, value: index
    for i, num in enumerate(nums):
        difference = target - num
        if difference in nums_map:
            add_indexes.append(nums_map[difference])
            add_indexes.append(i)
        else:
            nums_map[num] = i

    print(nums_map)

    return add_indexes
