__author__ = 'Young'
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#For example, given n = 3, a solution set is:

#"((()))", "(()())", "(())()", "()(())", "()()()"

class Solution022:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        answer = []
        self.generate(n, n, "" , answer)

        return answer

    def generate(self, left, right, str, answer):
        if left == 0 and right == 0:
            answer.append(str)
            return
        if left > 0:
            self.generate( left -1, right , str + "(" , answer)
        if right > 0 and right > left:
            self.generate( left, right-1, str + ")" , answer)
        return