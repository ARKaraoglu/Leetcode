# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        openingPar = ["(","[","{"]
        closingPar = [")", "]", "}"]
        order = []
        for x in range(0, len(s)):
            if x == 0 and s[x] in closingPar:
                return False

            if s[x] in openingPar:
                order.insert(0, s[x])

            if s[x] in closingPar:
                if len(order) == 0:
                    return False
                elif closingPar.index(s[x]) != openingPar.index(order[0]):
                    return False
                else:
                    order.pop(0)
        
        if len(order) > 0:
            return False
        else:
            return True
# @leet end
