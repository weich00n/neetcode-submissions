class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)

        #adj list with edge weight
        for u,v,w in times:
            adj[u].append((v,w))
        
        # current distance
        dist = {node: float('inf') for node in range(1, n+1)}

        # starting node
        q = deque([(k,0)])
        dist[k] = 0

        while q:
            node, time = q.popleft()

            # if the shortest path is already less no point
            if dist[node] < time:
                continue
            
            for nei, w in adj[node]:
                if time + w < dist[nei]:
                    dist[nei] = time + w
                    q.append((nei, time + w))
        
        res = max(dist.values())

        return res if res != float('inf') else -1