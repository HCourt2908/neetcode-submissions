class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prods = []
        mult = 1
        for x in nums:
            if len(prods) == 0:
                prods.append(1)
                mult*=x
            else:
                for i in range(len(prods)):
                    prods[i] *= x
                prods.append(mult)
                mult*=x
        return prods