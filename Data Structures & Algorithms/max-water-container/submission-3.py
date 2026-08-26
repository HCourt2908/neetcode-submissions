class Solution:
    def maxArea(self, heights: List[int]) -> int:

        area = 0
        
        i = 0

        while i < len(heights) - 1:

            j = i+1

            while j < len(heights):

                area = max(area, (j-i) * min(heights[j],heights[i]))

                j += 1

            i += 1

        
        return area
        