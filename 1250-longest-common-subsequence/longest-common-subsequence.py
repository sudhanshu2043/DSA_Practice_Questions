class Solution:
    def func(self,i,j,text1,text2,dp):
        if i==-1 or j==-1: return 0
        if dp[i][j]!=-1: return dp[i][j]
        if text1[i]==text2[j]:
            dp[i][j]=1+self.func(i-1,j-1,text1,text2,dp)
            return dp[i][j]
        dp[i][j]=max(self.func(i-1,j,text1,text2,dp),self.func(i,j-1,text1,text2,dp))
        return dp[i][j]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        return self.func(len(text1)-1,len(text2)-1,text1,text2,dp)
        