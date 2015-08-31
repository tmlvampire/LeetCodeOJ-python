__author__ = 'Young'

"""
Longest Valid Parentheses Total Accepted: 43283 Total Submissions: 206335 My Submissions Question Solution
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

class Solution032(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        bools = [False for char in s]

        stack=[]
        for i in range(len(s)):
            if s[i] == '(':
                bools[i] = False
                stack.append(i)
            else:
                if len(stack) != 0 and s[stack[len(stack)-1]] == '(':
                    bools[i] = True
                    bools[stack.pop()] = True
                else:
                    bools[i] = False
                    stack.append(i)
        max = 0
        i = 0
        while i < len(bools):
            if bools[i] == True:
                start = i
                while i < len(bools) and bools[i] == True:
                    i += 1
                end = i
                max = end - start if (end-start) > max else max
            else:
                i += 1

        return max