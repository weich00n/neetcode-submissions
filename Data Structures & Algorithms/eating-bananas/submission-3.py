import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = 1000000000

        def check(eat):
            time = 0

            for pile in piles:
                time += math.ceil(pile / eat)

            return time
        
        while l < r:
            mid = (l + r) // 2
            
            if check(mid) > h:
                l = mid + 1
            else:
                r = mid
        
        return l

