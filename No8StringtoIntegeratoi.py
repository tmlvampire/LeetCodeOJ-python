__author__ = 'Young'
# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases.
# If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
#
# Update (2015-02-10):
# The signature of the C++ function had been updated.
# If you still see your function signature accepts a const char * argument,
# please click the reload button  to reset your code definition.
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
# and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
class Solution:
    # @return an integer
    def myAtoi(self, str):
    # filter blank
        while len(str) != 0 and str[0] == ' ':
            str = str[1:]
        resultStr = str
        if len(resultStr) == 0:
            return 0
        minus = False
    # the first non-number char , get minus or plus , if other char, reply none
        firstChar = resultStr[0]
        if firstChar == '+':
            minus = False
            resultStr = resultStr[1:]
        elif firstChar == '-':
            minus = True
            resultStr = resultStr[1:]
        elif firstChar >= '0' and firstChar <= '9':
            pass
        else:
            return 0
    # filter first a few 0
    # cal the number
        resultInt = 0
        for i in range(len(resultStr)):
            if resultStr[i] >= '0' and resultStr[i] <= '9':
                resultInt = resultInt * 10 + ( ord(resultStr[i]) - 48 )
            else:
                break

        if minus == True:
            resultInt *= -1

        if resultInt >= 2147483647:
            return 2147483647
        if resultInt <= -2147483648:
            return -2147483648

        return resultInt


a = "1234"
b = a[0]
if b >= '0' and b <= '9':
    print "true"