__author__ = 'yanyang'
import unittest
from No8StringtoIntegeratoi import Solution

class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        test = Solution()

    def test_solution(self):
        errorMessage = "Not equal"
        x = Solution()
        self.assertEqual(-12345, x.atoi("-12345"), errorMessage)
        self.assertEqual(1234, x.atoi("+1,234"), errorMessage)
        self.assertEqual(0, x.atoi("   "), errorMessage)
        self.assertEqual(-8, x.atoi("       -008"))
        self.assertEqual(0, x.atoi("      000000"))

    def tearDown(self):
        test = Solution()

if __name__ == '__main__':
    unittest.main