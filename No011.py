__author__ = 'Young'


#Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

#Note: You may not slant the container.

class Solution11:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        length = len(height)
        low = 0
        high = length - 1
        maxArea = 0
        while low < high:
            maxArea = max( maxArea , (high - low) * min(height[high] , height[low]))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1

        return maxArea
