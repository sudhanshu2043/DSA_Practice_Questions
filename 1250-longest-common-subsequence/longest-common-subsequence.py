class Solution:
    def func(self,s1,s2,dp):
        n = len(s1)
        m = len(s2)
        for ind1 in range(1,n+1):
            for ind2 in range(1,m+1):
                #match
                if s1[ind1-1]==s2[ind2-1]:
                    dp[ind1][ind2]= 1+dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2]= max(dp[ind1][ind2-1],dp[ind1-1][ind2])
        return dp[n][m]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        return self.func(text1,text2,dp)