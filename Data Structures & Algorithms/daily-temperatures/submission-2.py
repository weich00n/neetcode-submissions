class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                idx = stack.pop()[1]
                res[idx] = i - idx
            stack.append((temp, i))
        
        return res
