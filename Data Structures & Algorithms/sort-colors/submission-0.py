class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = -1
        r = len(nums)

        curr = 0

        while curr < r :
            if nums[curr] == 0:
                nums[l+1], nums[curr] = nums[curr], nums[l+1]
                l += 1
                curr += 1
            elif nums[curr] == 2:
                nums[r-1], nums[curr] = nums[curr], nums[r-1]
                r -= 1
            else:
                curr += 1
        
        

            
        