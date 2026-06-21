class Solution:
    def isValid(self,image,i,j):
        n,m=len(image),len(image[0])
        return 0<=i<n and 0<=j<m

    def func(self,image,sr,sc,oriColor,color,vis):
        if image[sr][sc]!=oriColor:
            return False
        image[sr][sc]=color
        vis[sr][sc]=1
        #explore all direction
        delRow=[-1,0,+1,0]
        delCol=[0,+1,0,-1]
        for i in range(4):
            newRow=sr+delRow[i]
            newCol=sc+delCol[i]
            if self.isValid(image,newRow,newCol) and image[newRow][newCol]==oriColor and vis[newRow][newCol]==-1:
                self.func(image,newRow,newCol,oriColor,color,vis)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color: return image
        n,m=len(image),len(image[0])
        vis=[[-1]*m for _ in range(n)]
        oriColor=image[sr][sc]
        self.func(image,sr,sc,oriColor,color,vis)
        return image