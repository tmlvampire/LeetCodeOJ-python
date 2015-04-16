__author__ = 'Young'
import unittest
from No009PalindromeNumber import Solution

class No9TestCase(unittest.TestCase):

    def test_solution(self):
        x = Solution()
        print 0
        self.assertEqual( True , x.isPalindrome(0))
        print 1230321
        self.assertEqual( True , x.isPalindrome(1230321))
        print 123321
        self.assertEqual( True , x.isPalindrome(123321))
        print 12321
        self.assertEqual( True , x.isPalindrome(12321))
        print 989898989
        self.assertEqual( True , x.isPalindrome(989898989))
        print 88888
        self.assertEqual( True , x.isPalindrome(88888))


        print 1000021
        self.assertEqual( False , x.isPalindrome(1000021))
        print 123456
        self.assertEqual( False , x.isPalindrome(123456))
        print 1021
        self.assertEqual( False , x.isPalindrome(1021))

if __name__ == '__main__':
    unittest.main