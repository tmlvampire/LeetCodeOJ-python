__author__ = 'Young'


# Determine whether an integer is a palindrome. Do this without extra space.

#click to show spoilers.

#Some hints:
#Could negative integers be palindromes? (ie, -1)

#If you are thinking of converting the integer to string, note the restriction of using extra space.

#You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

#There is a more generic way of solving this problem.


class Solution9:
    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):

        if x < 0:
            return False
        elif x >= 0 and x<= 9:
            return True
        elif x % 10 == 0:
            return False
        else:
            bigten = 10
            while bigten*10 < x:
                bigten *= 10
            smallten = 10

            while smallten <= bigten:

                big = x / bigten
                big %= 10

                small = x % smallten
                small = small / (smallten/10)

                if big != small:
                    return False
                else:
                    bigten /= 10
                    smallten *= 10

            return True
