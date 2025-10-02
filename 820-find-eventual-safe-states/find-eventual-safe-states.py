from typing import List

class Solution:
    def dfs(self, node, graph, vis, pathvis, safe):
        vis[node] = 1
        pathvis[node] = 1
        for nei in graph[node]:
            if not vis[nei]:
                if self.dfs(nei, graph, vis, pathvis, safe):
                    return True   # cycle found
            elif pathvis[nei]:
                return True       # back edge = cycle
        pathvis[node] = 0
        safe[node] = 1   # mark as safe if no cycle detected in its path
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0] * n
        pathvis = [0] * n
        safe = [0] * n   # 1 = safe, 0 = unsafe/cycle
        for i in range(n):
            if not vis[i]:
                self.dfs(i, graph, vis, pathvis, safe)
        ans = [i for i in range(n) if safe[i] == 1]
        return ans
