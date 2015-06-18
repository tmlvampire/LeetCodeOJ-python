__author__ = 'Young'
#Given a sorted array, remove the duplicates in place such that each element appear only once
# and return the new length.

#Do not allocate extra space for another array, you must do this in place with constant memory.

#For example,
#Given input array nums = [1,1,2],

#Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.


class Solution026:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):

        length = len(nums)
        if length <= 1: return length

        first = 0
        second = 1

        while second < length:
            while second < length and nums[second] == nums[first]:
                second += 1
            if second == length: break

            first += 1
            if first != second:
                temp = nums[first]
                nums[first] = nums[second]
                nums[second] = temp
                second += 1

        return first+1



