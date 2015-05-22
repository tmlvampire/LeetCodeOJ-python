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
    assert( x.myAtoi("   +0 123") == 0 , errorMessage)
    assert( x.myAtoi("") == 0 , errorMessage)
    assert(-12345 == x.myAtoi("-12345"), errorMessage)
    assert(1 == x.myAtoi("+1,234"), errorMessage)
    assert(0 == x.myAtoi("   "), errorMessage)
    assert(-8 == x.myAtoi("       -008"))
    assert(0 == x.myAtoi("      000000"))

def test_9():
    x = Solution9()
    print 0
    assert( True , x.isPalindrome(0))
    print 1230321
    assert( True , x.isPalindrome(1230321))
    print 123321
    assert( True , x.isPalindrome(123321))
    print 12321
    assert( True , x.isPalindrome(12321))
    print 989898989
    assert( True , x.isPalindrome(989898989))
    print 88888
    assert( True , x.isPalindrome(88888))
    print 1000021
    assert( False , x.isPalindrome(1000021))
    print 123456
    assert( False , x.isPalindrome(123456))
    print 1021
    assert( False , x.isPalindrome(1021))

def test_10():
    x = Solution10()
    assert(False, x.isMatch("aa","a"))
    assert(True , x.isMatch("aa","aa"))
    assert(False , x.isMatch("aaa","aa"))
    assert(True , x.isMatch("aa","a*"))
    assert(True , x.isMatch("aa",".*"))
    assert(True , x.isMatch("ab",".*"))
    assert(True , x.isMatch("aab","c*a*b"))
