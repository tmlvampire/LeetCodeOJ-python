__author__ = 'Young'

#Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        listchar = []
        listmax=[]
        max = 0
        position = 1
        listmax.append(0)
        for char in s:
            if listchar.__contains__(char):
                lastposition = listchar.index(char) + 1
                listmax.append(len(listchar) - lastposition + 1)
                del listchar[0:listchar.index(char) + 1]
            else:
                listmax.append(listmax[position-1]+1)

            listchar.append(char)
            if listmax[position] > max:
                max = listmax[position]
            position += 1
        return max





test = Solution()
print test.lengthOfLongestSubstring("bbbbbb")
#x = [1,2,3,4,5]
#print x[:3]