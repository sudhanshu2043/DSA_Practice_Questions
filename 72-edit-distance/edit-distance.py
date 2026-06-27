class Solution:
    def func(self,s1,s2,i,j,dp):
        if i<0: return j+1
        if j<0: return i+1
        if dp[i][j]!=-1: return dp[i][j]
        if s1[i]==s2[j]:
            dp[i][j]=self.func(s1,s2,i-1,j-1,dp)
            return dp[i][j]
        else:
            insert=self.func(s1,s2,i,j-1,dp)
            delete=self.func(s1,s2,i-1,j,dp)
            replace=self.func(s1,s2,i-1,j-1,dp)
            dp[i][j]=1+min(insert,delete,replace)
        return dp[i][j]
    def minDistance(self, word1: str, word2: str) -> int:
        n,m=len(word1),len(word2)
        dp=[[-1]*m for _ in range(n)]
        return self.func(word1,word2,len(word1)-1,len(word2)-1,dp)