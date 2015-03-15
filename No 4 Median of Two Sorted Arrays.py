__author__ = 'Young'

# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        return A[1]



test = Solution()
print test.findMedianSortedArrays([1,2],[2,3])
