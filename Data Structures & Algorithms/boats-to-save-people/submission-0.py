class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 2 people at each time!
        people.sort()

        res, l = 0, 0
        r = len(people) - 1

        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        
        return res