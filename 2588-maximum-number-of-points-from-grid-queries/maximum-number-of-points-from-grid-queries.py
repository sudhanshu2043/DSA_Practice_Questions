class Solution:
    def __init__(self):
        self.delRow=[0,1,0,-1]
        self.delCol=[1,0,-1,0]
    def isValid(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(grid), len(grid[0])
        ans = {}
        minHeap = [(grid[0][0], 0, 0)]  # (value, row, col)
        vis = [[False] * m for _ in range(n)]
        vis[0][0] = True
        count = 0
        
        sorted_queries = sorted(queries)
        
        for q in sorted_queries:
            while minHeap and minHeap[0][0] < q:
                val, i, j = heappop(minHeap)
                count += 1
                
                for k in range(4):
                    newRow, newCol = i + self.delRow[k], j + self.delCol[k]
                    if self.isValid(newRow, newCol, n, m) and not vis[newRow][newCol]:
                        vis[newRow][newCol] = True
                        heappush(minHeap, (grid[newRow][newCol], newRow, newCol))
            
            ans[q] = count
        
        return [ans[q] for q in queries]

