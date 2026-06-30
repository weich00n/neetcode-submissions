class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0

        l = 0
        r = len(heights) - 1

        while l < r:

            currVol = (r - l) * min(heights[l], heights[r])
            
            maxVol = max(maxVol, currVol)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxVol
            
