__author__ = 'Young'
#Given an integer, convert it to a roman numeral.

#Input is guaranteed to be within the range from 1 to 3999.


class Solution12:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        tableX = [
            ["", "M" , "MM" , "MMM"],
            ["", "C", "CC", "CCC" , "CD" , "D" , "DC" , "DCC" , "DCCC" , "CM"],
            ["", "X", "XX", "XXX", "XL" , "L", "LX", "LXX", "LXXX", "XC"],
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        ]
        thousand = num / 1000
        hundred = (num % 1000) / 100
        ten = (num % 100) / 10
        one = num % 10

        return tableX[0][thousand] + tableX[1][hundred] + tableX[2][ten] + tableX[3][one]





