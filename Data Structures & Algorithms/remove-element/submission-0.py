class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = 0

        for i in range(len(nums)):
            if nums[r] == val:
                r += 1
            else:
                nums[l] = nums[r]
                l += 1
                r += 1
        
        return l