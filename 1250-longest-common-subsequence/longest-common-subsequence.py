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
        for i in range(n+1):
            dp[i][0]=0
        for j in range(m+1):
            dp[0][j]=0
        # Base case
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
        