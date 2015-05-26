__author__ = 'Young'

#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

#    For example, given array S = {-1 2 1 -4}, and target = 1.

#    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution16:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        if result == target:
            return target
        for i in range(len(nums)-2):
            small = i + 1
            big = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while small < big:
                sumx = nums[i] + nums[big] + nums[small]
                close = sumx - target
                if abs(close) < abs(result - target):
                    result = sumx
                if close == 0:
                    return target
                elif close > 0:
                    temp = nums[big]
                    big -= 1
                    while big > small and nums[big] == temp:
                        big -= 1
                elif close < 0:
                    temp = nums[small]
                    small += 1
                    while small < big and nums[small] == temp:
                        small += 1
        return result