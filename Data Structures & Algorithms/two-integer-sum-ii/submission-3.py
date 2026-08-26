class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lPointer = 0
        rPointer = len(numbers) - 1

        while True:
            if numbers[lPointer] + numbers[rPointer] < target:
                lPointer += 1
            elif numbers[lPointer] + numbers[rPointer] > target:
                rPointer -= 1
            else:
                break
        return [lPointer+1, rPointer+1]