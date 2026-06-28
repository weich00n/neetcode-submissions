class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []
        n = len(nums)
        for num in nums:
            count[num] += 1
        
        buckets = [[] for _ in range(n+1)]

        for num in count:
            buckets[count[num]].append(num)
        
        for i in range(n, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res