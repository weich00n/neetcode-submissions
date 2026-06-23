class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            # if seen, replace
            if n in seen:
                return False
            seen.add(n)
            # calculate sum of square of digits
            total, num = 0, n
            while num > 0:
                total += (num % 10) ** 2
                num //= 10
            
            # replace
            n = total
        
        return True
