class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A,B = nums1, nums2
        total = len(A) + len(B)

        if len(A) > len(B):
            A,B = B,A

        l = 0
        r = len(A) - 1
        while True:
            # index of mids
            i = (l + r) // 2
            # subtract 2 --> both arrays start at zero
            j = (total // 2) - i - 2

            A_left = A[i] if i >= 0 else float('-inf')
            A_right = A[i+1] if i+1 < len(A) else float('inf')
            B_left = B[j] if j >= 0 else float('-inf')
            B_right = B[j+1] if j+1 < len(B) else float('inf')

            # a valid partition A_left <= B_right and B_left <= A_right
            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 1:
                    return min(A_right, B_right)
                else:
                    return (min(A_right, B_right) + max(A_left, B_left)) / 2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
                
 

        