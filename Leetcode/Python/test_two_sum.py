import pytest
from two_sum import two_sum

@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([5, 11, 3, 4], 15, [1, 3]),
        ([8, 2, 7, 4], 6, [1,3])
    ]
)
def test_twoSum(nums, target, expected):
    assert two_sum(nums, target) == expected
