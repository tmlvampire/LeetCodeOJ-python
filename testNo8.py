__author__ = 'yanyang'
import unittest
from No8StringtoIntegeratoi import Solution

class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        test = Solution()

    def test_solution(self):
        errorMessage = "Not equal"
        x = Solution()
        self.assertEqual(0, x.myAtoi("   +0 123") , errorMessage)
        self.assertEqual(0, x.myAtoi("") , errorMessage)
        self.assertEqual(-12345, x.myAtoi("-12345"), errorMessage)
        self.assertEqual(1, x.myAtoi("+1,234"), errorMessage)
        self.assertEqual(0, x.myAtoi("   "), errorMessage)
        self.assertEqual(-8, x.myAtoi("       -008"))
        self.assertEqual(0, x.myAtoi("      000000"))

    def tearDown(self):
        test = Solution()

if __name__ == '__main__':
    unittest.main