class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                res += max(0, leftMax -height[l])
                l += 1
                leftMax = max(height[l], leftMax)
            else:
                res += max(0, rightMax -height[r])
                r -= 1
                rightMax = max(rightMax, height[r])
        
        return res


        #O(n) space, O(n) time complexity
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i-1])
        
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
        
        res = 0

        for i in range(n):
            res += max(0, min(leftMax[i], rightMax[i]) - height[i])

        return res