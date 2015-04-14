__author__ = 'yanyang'
import unittest
from No8StringtoIntegeratoi import Solution

class SolutionTestCase(unittest.TestCase):



    def test_solution(self):
        x = Solution()
        self.assertEqual( 0 , x.atoi("-12345"), 'Not equallll')
        # assert 1234==test.atoi("+1,234")
        # assert 0==test.atoi("")
        # assert 0==test.atoi("   ")
        # assert -8, test.atoi("   -0000008")
        # assert 0, test.atoi("        000000")


if __name__ == '__main__':
    unittest.main