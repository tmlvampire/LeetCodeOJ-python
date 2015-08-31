__author__ = 'Young'

'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2 -> 2,1,3 -> 2,3,1 -> 3,1,2 -> 3,2,1
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1 -> 5,1,1
'''

class Solution031(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 1:
            return

        position = length - 2

        while position >= 0:
            if nums[position] < nums[position+1]:
                break
            else:
                position -= 1
                continue

        pa = position

        if pa == -1:
            nums.reverse()
            return

        pb = length - 1
        while nums[pb] <= nums[pa]:
            pb -= 1

        x = nums[pa]
        nums[pa] = nums[pb]
        nums[pb] = x

        pa += 1
        pb = length-1
        while pa < pb:
            x = nums[pa]
            nums[pa] = nums[pb]
            nums[pb] = x
            pa += 1
            pb -= 1