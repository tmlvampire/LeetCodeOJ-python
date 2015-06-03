__author__ = 'Young'

#Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

#The brackets must close in the correct order,
# "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution20:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if len(s) == 0:
            return True
        stack = []
        for i in range(len(s)):
            if s[i]=='[' or s[i]=='(' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ']' or s[i] == '}' or s[i] == ')':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if (temp == '(' and s[i] == ')') or (temp == '{' and s[i] == '}') or (temp == '[' and s[i] == ']'):
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
