__author__ = 'Young'
import math
from No1 import Solution1
from No2 import Solution2
from No2 import ListNode
from No3 import Solution3
from No4 import Solution4
from No5 import Solution5
from No6 import Solution6
from No7 import Solution7
from No8StringtoIntegeratoi import Solution8
from No009PalindromeNumber import Solution9
from No010RegularExpressionMatching import Solution10
from No011 import Solution11
from No012 import Solution12
from No013 import Solution13
from No014 import Solution14
from No015 import Solution15
from No016 import Solution16
from No017 import Solution17
from No018 import Solution18
from No019 import Solution19
from No020 import Solution20
from No021 import Solution021

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def func(x):
	return x + 1

def test_answer():
	assert func(3) == 4

def test_1():
    x = Solution1()
    x.twoSum([3,2,4],6)

def test_2():
    test = Solution2()
    l1 = ListNode(9)
    l1.next = ListNode(8)

    l2 = ListNode(1)

    x =  test.addTwoNumbers(l1,l2)
    while x != None:
        print x.val
        x = x.next

def test_3():
    test = Solution3()
    print test.lengthOfLongestSubstring("bbbbbb")

def test_4():
    test = Solution4()
    print test.findMedianSortedArrays([1, 2, 6, 7,9], [3, 4, 5, 8,9])

def test_5():
    test = Solution5()
    print test.longestPalindrome("abcbe")
    print test.longestPalindrome("abb")
    print test.longestPalindrome("aab")
    print test.longestPalindrome("aaa")

def test_6():
    test = Solution6()
    print test.convert("abcd",1)

def test_7():
    test = Solution7()
    print int(math.pow(2,31)-1)
    print test.reverse(-10000000)

def test_8():
    errorMessage = "Not equal"
    x = Solution8()
    assert x.myAtoi("   +0 123") == 0
    assert x.myAtoi("") == 0
    assert -12345 == x.myAtoi("-12345")
    assert 1 == x.myAtoi("+1,234")
    assert 0 == x.myAtoi("   ")
    assert -8 == x.myAtoi("       -008")
    assert 0 == x.myAtoi("      000000")

def test_9():
    x = Solution9()
    print 0
    assert( True == x.isPalindrome(0))
    print 1230321
    assert( True == x.isPalindrome(1230321))
    print 123321
    assert( True == x.isPalindrome(123321))
    print 12321
    assert( True == x.isPalindrome(12321))
    print 989898989
    assert( True == x.isPalindrome(989898989))
    print 88888
    assert( True == x.isPalindrome(88888))
    print 1000021
    assert( False == x.isPalindrome(1000021))
    print 123456
    assert( False == x.isPalindrome(123456))
    print 1021
    assert( False == x.isPalindrome(1021))

def test_10():
    x = Solution10()
    assert(False == x.isMatch("aa","a") , "hello Error")
    assert(True == x.isMatch("aa","aa"))
    assert(False == x.isMatch("aaa","aa"))
    assert(True == x.isMatch("aa","a*"))
    assert(True == x.isMatch("aa",".*"))
    assert(True == x.isMatch("ab",".*"))
    assert(True == x.isMatch("aab","c*a*b"))
    assert(True == x.isMatch("",".*"))

def test_11():
    x = Solution11()
    assert x.maxArea([4,3,2,1,2,3,5]) == 24
    assert x.maxArea([4,3,2,1,2,3,1]) == 15

def test_12():
    x = Solution12()
    print x.intToRoman(999)
    print x.intToRoman(1999)
    print x.intToRoman(499)
    print x.intToRoman(1024)
    print x.intToRoman(0)
    print x.intToRoman(2048)
    print x.intToRoman(3001)

def test_13():
    x = Solution13()
    print x.romanToInt("CMXCIX")
    print x.romanToInt("")
    print x.romanToInt("MCMXCIX")
    print x.romanToInt("CDXCIX")
    print x.romanToInt("MMXLVIII")
    print x.romanToInt("MMMI")

def test_14():
    x = Solution14()
    assert "ab" == x.longestCommonPrefix(["abcd" , "abccc", "ab"])

def test_15():
    x = Solution15()
    print x.threeSum([-1,0,1,2,-1,-4])
    assert [[-1,-1,2],[-1,0,1]] == x.threeSum([-1,0,1,2,-1,-4])
    assert [[0,0,0]] == x.threeSum([0,0,0,0])
    assert [[-2,0,2],[-2,1,1]] == x.threeSum([-2,0,1,1,2])

def test_16():
    x = Solution16()
    assert 2 == x.threeSumClosest([-1, 2, 1, -4], 1)
    assert 2 == x.threeSumClosest([1, 1, 1, 0], -100)

def test_17():
    x = Solution17()
    assert [] == x.letterCombinations("")
    assert ['z', 'y', 'x', 'w'] == x.letterCombinations("9")
    assert ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'] == x.letterCombinations("23")

def test_18():
    x = Solution18()
    assert [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]] == x.fourSum([1, 0, -1, 0, -2, 2], 0)

def test_19():
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(5)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    x = Solution19()
    y = x.removeNthFromEnd(first, 2)
    assert y.val == 1
    assert y.next.val == 2
    assert y.next.next.val == 3
    assert y.next.next.next.val == 5

    x.removeNthFromEnd(None, 0)

    first = ListNode(1)
    second = ListNode(2)
    first.next = second

    x.removeNthFromEnd(first, 2)

def test_20():
    x = Solution20()
    assert True == x.isValid("[]{}[[]]{{}}")
    assert False == x.isValid("[]{}[[]]{{}}}}")
    assert True == x.isValid("")
    assert False == x.isValid("]")
    assert False == x.isValid("((])")

def test_21():
    x = Solution021
    a1 = ListNode(1)
    a2 = ListNode(3)
    a3 = ListNode(5)
    a1.next = a2
    a2.next = a3

    b1 = ListNode(0)
    b2 = ListNode(4)
    b3 = ListNode(6)
    b1.next = b2
    b2.next = b3

    x = Solution021()
    y = x.mergeTwoLists(a1, None)
    assert y.next.val == 3
    y = x.mergeTwoLists(a1, b1)
    assert y.next.val == 1
    y = x.mergeTwoLists(None, b1)
    assert y.next.val == 4
