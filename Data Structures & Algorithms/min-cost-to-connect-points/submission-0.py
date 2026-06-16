class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adjList = {i : [] for i in range(n)} # list of [cost, node]

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2,y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])
        
        visited = set()
        res = 0
        minHeap = [[0,0]] # cost and point
        
        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            
            res += cost
            visited.add(i)
            for neiCost, nei in adjList[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])
        
        return res