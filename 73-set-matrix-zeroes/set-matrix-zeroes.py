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
        row=[-1 for _ in range(n)]
        col=[-1 for _ in range(m)]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=0
                    col[j]=0
        for i in range(n):
            for j in range(m):
                if row[i]==0 or col[j]==0:
                    matrix[i][j]=0
        
        
        