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

class Solution10:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):
        length_s = len(s)
        length_p = len(p)
        if length_s == 0 or length_p == 0:
            return False
        statusMatrix = [[False for x in range(length_p+1)] for x in range(length_s+1)]
        statusMatrix[0][0] = True
        for j in range(1, length_p+1 , 1):
            if p[j-1] == '*':
                statusMatrix[0][j] = statusMatrix[0][j-2]
        for i in range( 1, length_s + 1, 1):
            for j in range( 1, length_p + 1 , 1):
                if p[j-1] != '*':
                    if statusMatrix[i-1][j-1] and ( p[j-1] == '.' or s[i-1] == p[j-1]):
                        statusMatrix[i][j] = True
                else:
                    if statusMatrix[i][j-2] or ( statusMatrix[i-1][j] and (p[j-2] == '.' or s[i-1] == p[j-2])):
                        statusMatrix[i][j] = True

        return statusMatrix[length_s][length_p]

a = Solution10()
print a.isMatch("aab", "c*a*b")