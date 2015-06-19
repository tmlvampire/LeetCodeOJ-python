__author__ = 'Young'

#Divide two integers without using multiplication, division and mod operator.

#If it is overflow, return MAX_INT.

class Solution029:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):

        print dividend
        print "/"
        print divisor
        print "="

        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if divisor == 0: return MAX_INT
        if dividend == 0: return 0

        fuhao = 1
        if dividend > 0 and divisor < 0:
            fuhao = -1
            divisor = -divisor
        elif dividend < 0 and divisor > 0:
            fuhao = -1
            dividend = -dividend
        elif dividend < 0 and divisor < 0:
            divisor = -divisor
            dividend = -dividend

        pow2 = 1
        powx = divisor
        while powx < MAX_INT and powx < dividend:
            pow2 <<= 1
            powx <<= 1

        plusResult = 0
        answer = 0
        while pow2 >= 1:
            plusResult += powx
            answer += pow2
            if plusResult > dividend:
                plusResult -= powx
                answer -= pow2

            pow2 >>= 1
            powx >>= 1

        if fuhao == -1:
            answer = -answer

        if answer > MAX_INT:
            answer = MAX_INT
        if answer < MIN_INT:
            answer = MIN_INT

        return answer
