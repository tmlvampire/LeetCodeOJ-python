__author__ = 'Young'

from No031 import Solution031
from No032 import Solution032

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

def test_32():
    x = Solution032()
    assert 10 == x.longestValidParentheses("((((()())))")
    assert 2 == x.longestValidParentheses("()")
    assert 4 == x.longestValidParentheses(")()()")
    assert 2 == x.longestValidParentheses("))))))))()")