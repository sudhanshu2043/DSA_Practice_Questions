class Solution:
    def func(self,nums,i,j,dp):
        if i>j: return 0
        maxi=-1e9
        if dp[i][j]!=-1: return dp[i][j]
        for ind in range(i,j+1):
            coin=(nums[i-1]*nums[ind]*nums[j+1])+self.func(nums,i,ind-1,dp)+self.func(nums,ind+1,j,dp)
            maxi=max(maxi,coin)
        dp[i][j]=maxi
        return dp[i][j]
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        m=len(nums)
        dp=[[-1]*m for _ in range(m)]
        return self.func(nums,1,m-2,dp)