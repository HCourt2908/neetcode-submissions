class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ints = dict()
        for x in nums:
            if x not in ints:
                ints[x] = 1
            else:
                ints[x] = ints[x] + 1
        
        orderedDict = sorted(ints.items(), key=lambda x: x[1])

        freqs = list()
        for i in range(k):
            freqs.append(orderedDict[len(orderedDict)-1-i][0])
        
        return freqs
            