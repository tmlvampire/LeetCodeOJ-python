__author__ = 'Young'

#Given an array and a value, remove all instances of that value in place and return the new length.

#The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution027:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        length = len(nums)
        if length == 0: return 0
        first = 0
        last = length-1
        while last >= 0 and nums[last] == val: last -= 1
        while first <= length-1 and nums[first] != val: first += 1
        if first - last > 1: return 0

        while first < last:
            temp = nums[first]
            nums[first] = nums[last]
            nums[last] = temp
            while nums[last] == val and last > 0: last -= 1
            while nums[first] != val and first < length-1: first += 1

        return first
