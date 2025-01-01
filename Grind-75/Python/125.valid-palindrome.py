# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:

        rightPointer = 0

        filteredString = ""
        for letter in s:
            if letter.isalnum():
                filteredString += letter.lower()
        
        filteredLength = len(filteredString)
        if filteredLength == 0:
            return True
        else:
            rightPointer = filteredLength - 1

        for x in range(0, filteredLength):
            if filteredString[x] != filteredString[rightPointer]:
                return False
            else:
                rightPointer -= 1

            if x == rightPointer:
                break

        return True



# @leet end
