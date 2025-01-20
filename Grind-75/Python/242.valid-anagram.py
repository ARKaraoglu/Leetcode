# @leet start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sDict = {}
        tDict = {}

        if len(s) != len(t):
            return False

        for x in range(0, len(s)):
            if s[x] in sDict:
                sDict[s[x]] += 1
            else:
                sDict[s[x]] = 1

            if t[x] in tDict:
                tDict[t[x]] += 1
            else:
                tDict[t[x]] = 1

        for letter, value in sDict.items():
            if letter not in tDict:
                return False
            
            else:
                if tDict[letter] != value:
                    return False

        return True

# @leet end
