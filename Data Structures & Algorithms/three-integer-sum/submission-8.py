class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = []

        sortNums = nums
        sortNums.sort()

        for i in range(len(sortNums)-2):
            lPointer = i+1
            rPointer = len(sortNums) - 1
            while(lPointer < rPointer):
                if sortNums[i] + sortNums[lPointer] + sortNums[rPointer] < 0:
                    lPointer += 1
                elif sortNums[i] + sortNums[lPointer] + sortNums[rPointer] > 0:
                    rPointer -= 1
                else:
                    trip = [sortNums[i], sortNums[lPointer], sortNums[rPointer]]
                    if trip not in triples:
                        triples.append(trip)
                    lPointer += 1
                    rPointer -= 1
        return triples
