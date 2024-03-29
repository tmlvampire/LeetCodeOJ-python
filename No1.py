__author__ = 'Young'

# Given an array of integers, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution1:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dictionary = {}
        position = 0
        for number in num:
            position += 1
            if dictionary.has_key(target-number):
                return (dictionary[target-number],position)
            dictionary[number] = position

        return dictionary


# xyz = Solution()
#
# print xyz.twoSum([3,2,4],6)