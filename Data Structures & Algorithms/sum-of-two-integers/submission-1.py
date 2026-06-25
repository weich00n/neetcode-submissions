class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # 01
        # 01
        # carry = 1, 1 ^ 1 = 0

        #  100
        #  111
        # 1011 carry = 1

        mask = 0xFFFFFFFF

        carry = 0
        res = 0

        for i in range(32):
            a_bit = (a>>i) & 1
            b_bit = (b>>i) & 1

            curr_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) or (carry & b_bit) or (a_bit & carry)

            if curr_bit:
                res |= (1 << i)
        
        # if ans is negative
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        
        return res