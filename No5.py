# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
# and there exists one unique longest palindromic substring.

class Solution5:
    # @return a string
    def longestPalindrome(self, s):
        lenofstr = len(s)
        newstr = []
        newstr.append('*')
        i = 0
        for x in range(lenofstr):
            if x != lenofstr-1:
                newstr.append(s[x])
                newstr.append('#')
            else:
                newstr.append(s[x])
                newstr.append('#')

        rightbound = 0  # record the right position
        pi = 1          # record the center
        i = 1           # start from the 1 in newstr, since the 0 in newstr is char *
        intarray = []   # the assist array to record all palindrome
        intarray.insert(0, 0)
        for x in range(1, len(newstr), 1):
            if rightbound > x:
                intarray.insert(x, min(rightbound-x, intarray[2*pi - x]))
            else:
                intarray.insert(x, 1)
            while x-intarray[x] > 0 and x+intarray[x] < len(newstr) and newstr[x - intarray[x]] == newstr[x + intarray[x]] :
                intarray[x] += 1

            if (x+intarray[x]) > rightbound:
                pi = x
                rightbound = x+intarray[x]

        length = max(intarray)
        position = intarray.index(length)

        resultstr = newstr[position-length+1: position+length]

        print newstr
        print intarray
        print resultstr

        resultstr = list(filter(lambda x: x != '*' and x != '#', resultstr))

        return ''.join(resultstr)

