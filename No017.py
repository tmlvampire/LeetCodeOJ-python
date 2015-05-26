__author__ = 'Young'

#Given a digit string, return all possible letter combinations that the number could represent.

#A mapping of digit to letters (just like on the telephone buttons) is given below.


#Input:Digit string "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#Note:
#Although the above answer is in lexicographical order, your answer could be in any order you want.

class Solution17:
    # @param {string} digits
    # @return {string[]}


    def letterCombinations(self, digits):
        dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["o", "n", "m"],
            "7": ["r", "q", "p", "s"],
            "8": ["v", "u", "t"],
            "9": ["z", "y", "x", "w"]
        }
        result = []
        if len(digits) == 0: return result
        self.getResult( result, digits, 0, "", dict)
        return result

    def getResult(self, result, digits, index, current, dict):
        array = dict[digits[index]]
        for i in range(len(array)):
            current += array[i]
            if index == len(digits)-1:
                result.append(current)
            else:
                self.getResult(result, digits, index+1, current, dict)
            current = current[:-1]
        return



x = Solution17()
b = x.letterCombinations("")
print b
print len(b)

b = x.letterCombinations("9")
print b
print len(b)

b = x.letterCombinations("23")
print b
print len(b)