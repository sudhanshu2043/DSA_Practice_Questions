class Solution:
    def nCr(self,row,col):
        res=1
        n=row-1
        r=col-1
        for i in range(r):
            res*=(n-i)
            res=res//(i+1)
        return res
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for row in range(1,numRows+1):
            temp=[]
            for col in range(1,row+1):
                temp.append(self.nCr(row,col))
            ans.append(temp)
        return ans