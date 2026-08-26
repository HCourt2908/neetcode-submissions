class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list()
        y = list()
        for i in s:
            x.append(i)
        for j in t:
            y.append(j)
        return sorted(x) == sorted(y)
        