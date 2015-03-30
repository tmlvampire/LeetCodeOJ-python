__author__ = 'Young'

# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if len(A) + len(B) <= 4:
            C = A + B
            C.sort()
            return C[len(C)/2]
        else:
            m = len(A)
            n = len(B)
            if A[m/2] == B[n/2]:
                return A[m/2]
            elif A[m/2] > B[n/2]:
                x = min(m/2, n/2)
                return Solution.findMedianSortedArrays(self, A[0:m-x], B[x:n])
            elif A[m/2] < B[n/2]:
                x = min(m/2, n/2)
                return Solution.findMedianSortedArrays(self, A[x:m], B[0:n-x])
            return 0



test = Solution()
print test.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8])