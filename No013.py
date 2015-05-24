__author__ = 'Young'

#Given a roman numeral, convert it to an integer.

#Input is guaranteed to be within the range from 1 to 3999.

class Solution13:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        result = 0
        tableX = [
            ['M' , 1000],
            ['D' , 500],
            ['C' , 100],
            ['L' , 50],
            ['X' , 10],
            ['V' , 5],
            ['I' , 1]
        ]
        tableY = [
            ['CD' , 200],
            ['CM' , 200],
            ['XL' , 20],
            ['XC' , 20],
            ['IV' , 2],
            ['IX' , 2]
        ]

        for i in range(len(tableX)):
            result +=  s.count(tableX[i][0]) * tableX[i][1]

        for i in range(len(tableY)):
            result -= s.count(tableY[i][0]) * tableY[i][1]

        return result


x = Solution13()
print x.romanToInt("CMXCIX")
print x.romanToInt("")
print x.romanToInt("MCMXCIX")
print x.romanToInt("CDXCIX")
print x.romanToInt("MMXLVIII")
print x.romanToInt("MMMI")