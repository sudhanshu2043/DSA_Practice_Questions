from typing import List

class Solution:
    def dfs(self, node, adj, vis, pathVis):
        """Detects cycle using DFS"""
        vis[node] = 1       # Mark node as visited
        pathVis[node] = 1    # Mark node as part of recursion stack

        for it in adj[node]:
            if not vis[it]:  # If not visited, recurse
                if self.dfs(it, adj, vis, pathVis):
                    return True  # Cycle detected
            elif pathVis[it]:  # If already in recursion stack, cycle exists
                return True
        
        pathVis[node] = 0  # Remove from recursion stack after visiting all neighbors
        return False  # No cycle detected

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        # Build adjacency list
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])

        vis = [0] * numCourses     # Visited array
        pathVis = [0] * numCourses  # Recursion stack tracking

        # Run DFS for all unvisited nodes
        for i in range(numCourses):
            if not vis[i]:
                if self.dfs(i, adj, vis, pathVis):
                    return False  # If cycle found, courses can't be finished

        return True  # No cycle detected, all courses can be finished
