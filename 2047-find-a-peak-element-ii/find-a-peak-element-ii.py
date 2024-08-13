class Solution:
    def maxIndex(self,mat,n,m,mid):
        ans=-1
        index=-1
        for i in range(n):
            if mat[i][mid]>ans:
                ans=mat[i][mid]
                index=i
        return index

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        low,high=0,m-1
        while low<=high:
            mid=(high+low)//2
            row=self.maxIndex(mat,n,m,mid)
            left=-1
            if mid-1>=0:
                left=mat[row][mid-1]
            right=-1
            if mid+1<m:
                right=mat[row][mid+1]
            if mat[row][mid]>left and mat[row][mid]>right:
                return [row,mid]
            elif mat[row][mid]<left:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]
        