from typing import List

class Solution:
    def __init__(self):
        # Only allow movement in 4 directions: Up, Right, Down, Left
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, row, col, grid):
        n, m = len(grid), len(grid[0])
        return 0 <= row < n and 0 <= col < m

    def dfs(self, row, col, grid, vis):
        vis[row][col] = 1
        for i in range(4):  # Only 4 directions now
            newRow = row + self.delRow[i]
            newCol = col + self.delCol[i]
            if self.isValid(newRow, newCol, grid) and grid[newRow][newCol] == '1' and not vis[newRow][newCol]:
                self.dfs(newRow, newCol, grid, vis)

    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        count = 0

        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == '1':
                    self.dfs(i, j, grid, vis)
                    count += 1  # One complete island found
        return count
