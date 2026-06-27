class Solution:
    def func(self,s,t,i,j,dp):
        if j<0: return 1
        if i<0: return 0
        if dp[i][j]!=-1: return dp[i][j]
        if s[i]==t[j]:
            dp[i][j] =(self.func(s,t,i-1,j-1,dp)+self.func(s,t,i-1,j,dp))
        else:
            dp[i][j] = self.func(s,t,i-1,j,dp)
        return dp[i][j]
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)
        dp=[[-1]*m for _ in range(n)]
        return self.func(s,t,len(s)-1,len(t)-1,dp)