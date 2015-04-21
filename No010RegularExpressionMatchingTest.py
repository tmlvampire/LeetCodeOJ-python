__author__ = 'Young'
import unittest
from No010RegularExpressionMatching import Solution
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true
class test10(unittest.TestCase):
    def test_Solution(self):
        x = Solution()
        self.assertEqual(False, x.isMatch("aa","a"))
        self.assertEqual(True , x.isMatch("aa","aa"))
        self.assertEqual(False , x.isMatch("aaa","aa"))
        self.assertEqual(True , x.isMatch("aa","a*"))
        self.assertEqual(True , x.isMatch("aa",".*"))
        self.assertEqual(True , x.isMatch("ab",".*"))
        self.assertEqual(True , x.isMatch("aab","c*a*b"))

if __name__ == '__main__':
    unittest.main


