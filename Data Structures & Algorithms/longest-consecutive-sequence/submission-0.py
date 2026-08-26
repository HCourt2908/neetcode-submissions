class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0

        numSet = set()
        for x in nums:
            numSet.add(x)
        

        for i in range(len(nums)):
            if (nums[i]-1) not in numSet:

                seqCount = 1
                while True:
                    if (nums[i]+seqCount) in numSet:
                        seqCount += 1
                    else:
                        break
                longest = max(longest, seqCount)
        return longest
            