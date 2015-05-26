__author__ = 'Young'

#Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.

#Note:
#Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a  b  c  d)
#The solution set must not contain duplicate quadruplets.
#    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

#    A solution set is:
#    (-1,  0, 0, 1)
#    (-2, -1, 1, 2)
#    (-2,  0, 0, 2)

class Solution18:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, num, target):
        num.sort()
        result = []
        for i in xrange(len(num)-3):
            if num[i] > target/4.0:
                break
            if i > 0 and num[i] == num[i-1]:
                continue
            target2 = target - num[i]
            for j in xrange(i+1, len(num)-2):
                if num[j] > target2/3.0:
                    break
                if j > i+1 and num[j] == num[j-1]:
                    continue
                k = j + 1
                l = len(num) - 1
                target3 = target2 - num[j]
                # we should use continue not break
                # because target3 changes as j changes
                if num[k] > target3/2.0:
                    continue
                if num[l] < target3/2.0:
                    continue
                while k < l:
                    sum_value = num[k] + num[l]
                    if sum_value == target3:
                        result.append([num[i], num[j], num[k], num[l]])
                        kk = num[k]
                        k += 1
                        while k<l and num[k] == kk:
                            k += 1

                        ll = num[l]
                        l -= 1
                        while k<l and num[l] == ll:
                            l -= 1
                    elif sum_value < target3:
                        k += 1
                    else:
                        l -= 1
        return result


x = Solution18()
print x.fourSum([1, 0, -1, 0, -2, 2], 0)

