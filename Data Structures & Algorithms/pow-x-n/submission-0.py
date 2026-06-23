class Solution:
    def myPow(self, x: float, n: int) -> float:
        val = x
        total = 1
        negative = False
        if n < 0:
            negative = True
            n = - n
            
        while n > 0:
            check = n & 1
            if check:
                total *= val
            val *= val
            n >>= 1
        
        return total if not negative else 1/total