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
            if nums[i] > 0 or nums[big] < 0:
                return result
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while small < big:
                sumx = nums[i] + nums[big] + nums[small]
                if sumx == 0:
                    if [nums[i], nums[small], nums[big]] not in result:
                        result.append([nums[i], nums[small], nums[big]])
                    temp = nums[small]
                    small += 1
                    while small < big and nums[small] == temp:
                        small += 1
                elif sumx > 0:
                    temp = nums[big]
                    big -= 1
                    while big > small and nums[big] == temp:
                        big -= 1
                elif sumx < 0:
                    temp = nums[small]
                    small += 1
                    while small < big and nums[small] == temp:
                        small += 1
        return result

x = Solution15()
print x.threeSum([-1,0,1,2,-1,-4])
print x.threeSum([-2,0,1,1,2])
print x.threeSum([0,0,0,0])



