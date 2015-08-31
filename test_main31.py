__author__ = 'Young'
import math

from No031 import Solution031

def test_31():
    a = Solution031()
    nums = [1,2,3]
    a.nextPermutation(nums)
    assert [1,3,2] == nums
    a.nextPermutation(nums)
    assert [2,1,3] == nums
    a.nextPermutation(nums)
    assert [2,3,1] == nums
    a.nextPermutation(nums)
    assert [3,1,2] == nums
    a.nextPermutation(nums)
    assert [3,2,1] == nums
    a.nextPermutation(nums)
    assert [1,2,3] == nums
