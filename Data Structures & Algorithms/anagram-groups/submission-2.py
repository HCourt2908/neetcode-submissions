class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = []
        

        for string in strs:
            if len(anagramList) == 0:
                anagramList.append([string])
            else:
                found = False
                for anagram in anagramList:
                    x = []
                    for i in string:
                        x.append(i)
                    y = []
                    for i in anagram[0]:
                        y.append(i)
                    if sorted(x) == sorted(y):
                        anagram.append(string)
                        found = True
                if not found:
                    anagramList.append([string])

        return anagramList
    
    
        