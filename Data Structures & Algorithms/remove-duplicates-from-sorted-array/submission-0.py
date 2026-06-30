class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1
        n = len(nums)
        k = 1
        l = 0
        r = 1

        while r < n:
            while nums[l] == nums[r]:
                r += 1
                if r == n:
                    return k
            
            l += 1
            nums[l] = nums[r]
            k += 1
            r += 1
        
        return k