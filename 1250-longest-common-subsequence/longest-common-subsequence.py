class Solution:
    def func(self,s1,s2,ind1,ind2,dp):
        if ind1<0 or ind2<0: return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        #match
        if s1[ind1]==s2[ind2]:
            dp[ind1][ind2]= 1+self.func(s1,s2,ind1-1,ind2-1,dp)
        else:
            dp[ind1][ind2]= max(self.func(s1,s2,ind1,ind2-1,dp),self.func(s1,s2,ind1-1,ind2,dp))
        return dp[ind1][ind2]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        dp=[[-1]*m for _ in range(n)]
        return self.func(text1,text2,len(text1)-1,len(text2)-1,dp)