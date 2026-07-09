class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = len(nums) + 1

        l = 0 
        currSum = 0

        for r in range(0, len(nums)):
            currSum += nums[r]

            while currSum >= target:
                length = r - l + 1
                res = min(res, length)
                currSum -= nums[l]
                l += 1
        
        return res if res <= len(nums) else 0
    
        
        