__author__ = 'Young'

# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def updatesmall(self,array):
        return


    def updatebig(self,array):
        return
    # @return a float
    def findMedianSortedArrays(self, A, B):
        bigRootPile = []
        smallRootPile = []
        sizeA = len(A)
        sizeB = len(B)
        m = 0
        n = 0

        while m < sizeA or n < sizeB:
            if A[m] <= B[n] or n >= sizeB:
                x = A[m]
                m += 1
            elif A[m] > B[n] or m >= sizeA:
                x = B[n]
                n += 1

            if smallRootPile[0] >= bigRootPile[0]:
                smallRootPile[smallRootPile[0] + 1] = x
                smallRootPile[0] += 1
                updatesmall(smallRootPile)
            else:
                bigRootPile[bigRootPile[0] + 1] = x
                bigRootPile[0] += 1
                updatebig(bigRootPile)



        return A[1]






test = Solution()
print test.findMedianSortedArrays([1,2],[2,3])