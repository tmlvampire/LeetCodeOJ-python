__author__ = 'Young'

#Implement strStr().

#Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution028:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
