class Solution:
    def searchMatrix(self, grid: List[List[int]], target: int) -> bool:
        m, n = len(grid), len(grid[0])
        row, col = 0, n - 1  # Start from the top-right corner

        while row < m and col >= 0:
            if grid[row][col]==target:
                return True
            if grid[row][col] < target:  # If negative, count all below
                row += 1
            else:
                col-=1  

        return False