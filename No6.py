__author__ = 'Young'

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"
#Write the code that will take a string and make this conversion given a number of rows:

#string convert(string text, int nRows);
#convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution6:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        bigList = []
        for i in range(nRows):
            smallList = []
            bigList.append(smallList)
        x = nRows*2 - 2
        for i in range(len(s)):
            y = i%x
            if y > nRows-1:
                distance = y-nRows+1
            else:
                distance = (nRows-1)-y
            lineNumber = nRows-1-distance
            bigList[lineNumber].append(s[i])
        result = ""
        for i in range(nRows):
            result += "".join(bigList[i])
        return result

        print bigList

