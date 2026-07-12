class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        #get list
        if key not in self.hashmap:
            return ""
        
        ls = self.hashmap[key]

        l = 0
        r = len(ls)

        # returns largest timestamp_prev <= timestamp
        # if timestamp < all, l < 0
        while l < r:
            mid = (l + r) // 2
            if timestamp < ls[mid][0]:
                r = mid
            else:
                l = mid + 1

        return "" if l == 0 else ls[l - 1][1]





