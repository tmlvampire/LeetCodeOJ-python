__author__ = 'Young'

#Write a function to find the longest common prefix string amongst an array of strings.

class Solution14:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs: return ""

        s1 = min(strs)
        s2 = max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1





x = Solution14()
print x.longestCommonPrefix(["abcd" , "abccc", "ab"])