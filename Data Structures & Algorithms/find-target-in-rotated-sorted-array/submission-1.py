class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        #find min
        # 4 5 6 7 1 2 3
        # F F F F T T F
        while l < r:
            mid = (l +r) // 2
            
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        # l is low

        if nums[l] <= target <= nums[len(nums) - 1]:
            #search right
            l = l
            r = len(nums)-1
        else:
            #search left
            r = l - 1
            l = 0
            
        
        while l < r:
            mid = (l +r) // 2
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l if nums[l] == target else -1
