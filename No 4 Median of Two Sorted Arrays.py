__author__ = 'Young'

# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if m <= 3 or n <= 3:
            C = A + B
            C.sort()
            if (m+n)%2 == 0:
                return float((C[len(C)/2] + C[len(C)/2-1])/2.0)
            else:
                return C[len(C)/2]
        else:
            if A[m/2] == B[n/2]:
                if (m%2 == 1 and n%2 == 1) or (m+n)%2 ==1:
                    return A[m/2]
                else:
                    return float( (A[m/2] + max(A[m/2-1], B[n/2-1]))/2.0)
            elif A[m/2] > B[n/2]:
                x = min(m/2, n/2)-1
                return Solution.findMedianSortedArrays(self, A[0:m-x], B[x:n])
            elif A[m/2] < B[n/2]:
                x = min(m/2, n/2)-1
                return Solution.findMedianSortedArrays(self, A[x:m], B[0:n-x])
            return 0



test = Solution()
print test.findMedianSortedArrays([1, 2, 6, 7,9], [3, 4, 5, 8,9])