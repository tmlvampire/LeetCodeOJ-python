__author__ = 'Young'

#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note:
# Elements in a triple( a < b < c)must be in non-descending order a<=b<=c
# The solution set must not contain duplicate triplets.
#    For example, given array S = {-1 0 1 2 -1 -4},

#   A solution set is:
#   (-1, 0, 1)
#   (-1, -1, 2)

class Solution15:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(len(nums)-2):
            small = i + 1
            big = len(nums) - 1
            while small < big:
                sumx = nums[i] + nums[big] + nums[small]
                if sumx == 0:
                    if [nums[i], nums[small], nums[big]] not in result:
                        result.append([nums[i], nums[small], nums[big]])
                    small += 1
                    big -= 1
                elif sumx > 0:
                    big -= 1
                elif sumx < 0:
                    small += 1
        return result

x = Solution15()
print x.threeSum([-2,0,1,1,2])
print x.threeSum([0,0,0,0])



