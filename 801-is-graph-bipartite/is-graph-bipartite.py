from collections import deque
class Solution:
    def bfs(self,start, V, adj, color):
        q = deque()        
        q.append(start)
        color[start] = 0 
        while q:
            node = q.popleft()
            for it in adj[node]:
                if color[it] == -1:
                    color[it] = 1 - color[node]
                    q.append(it)
                elif color[it] == color[node]:                    
                    return False
        return True
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V=len(graph)
        color = [-1] * V
        for i in range(V):
            if color[i] == -1:
                if  self.bfs(i, 0, graph,color)==False:
                    return False
        return True