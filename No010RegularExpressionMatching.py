# coding=utf-8
__author__ = 'Young'

#Implement regular expression matching with support for '.' and '*'.

#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.

#The matching should cover the entire input string (not partial).

#The function prototype should be:
#bool isMatch(const char *s, const char *p)

#Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

class Solution:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):
        length = len(p)
        if length == 0:
            return False

        statusAll = []
        i = 0
        while i < length:
            statusOne = []
            statusOne.append(p[i])
            i += 1
            if i < length and p[i] == '*':
                    statusOne.append(p[i])
            statusAll.append(statusOne)










        return False
