__author__ = 'Young'
import math
from No030 import Solution030

def test_30():
    x = Solution030()
    assert [0,9] == x.findSubstring("barfoothefoobarman", ["foo", "bar"])