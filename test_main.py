__author__ = 'Young'
from No1 import Solution1

def func(x):
	return x + 1

def test_answer():
	a = ClassX(1, 2)
	assert func(3) == 4
	assert a.x == 1
	assert a.y == 2
	assert a.printx() == "Hello World!"

def test_1():
    x = Solution1()
    x.twoSum([3,2,4],6)

def test_2():
