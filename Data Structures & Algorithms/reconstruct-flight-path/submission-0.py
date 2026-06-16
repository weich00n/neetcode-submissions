class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        tickets.sort()

        for u,v in tickets:
            adjList[u].append(v)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if src not in adjList:
                return False
            
            temp = list(adjList[src])
            for i, v in enumerate(temp):
                adjList[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                res.pop()
                adjList[src].insert(i, v)
            
            return False
        
        dfs("JFK")

        return res
                
