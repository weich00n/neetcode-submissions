class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(lists):
            if len(lists) == 1:
                return lists
            
            mid = len(lists) // 2

            l1 = merge(lists[:mid])
            l2 = merge(lists[mid:])

            return sort(l1, l2)

        
        def sort(l1, l2):
            i = 0
            j = 0
            res = []
            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    res.append(l1[i])
                    i += 1
                else:
                    res.append(l2[j])
                    j += 1
            
            if i < len(l1):
                return res + l1[i:]
            else:
                return res + l2[j:]
        
        return merge(nums)

