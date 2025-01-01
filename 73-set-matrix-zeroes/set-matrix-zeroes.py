class Solution:
    def setrow(self,dummy,row,m):
        for i in range(m):
            dummy[row][i]=0
    def setcol(self,dummy,col,n):
        for i in range(n):
            dummy[i][col]=0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        dummy = [[-1 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    self.setrow(dummy,i,m)
                    self.setcol(dummy,j,n)
        for i in range(n):
            for j in range(m):
                if dummy[i][j]==0:
                    matrix[i][j]=0
        
        
        