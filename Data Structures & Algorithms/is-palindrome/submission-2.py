class Solution:
    def isPalindrome(self, s: str) -> bool:
        modStr = ""
        for x in s:
            if x.isalnum():
                modStr += x.lower()
        
        leftP = 0
        rightP = len(modStr) - 1

        while leftP <= rightP:
            if modStr[leftP] != modStr[rightP]:
                return False
            leftP += 1
            rightP -= 1
        return True