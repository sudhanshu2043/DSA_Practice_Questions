class Solution:
    def func(self,nums,i,j,dp):
        m=len(nums)
        for i in range(m-2,0,-1):
            for j in range(i,m-1):
                maxi=-1e9
                if i>j: continue
                for ind in range(i,j+1):
                    coin=(nums[i-1]*nums[ind]*nums[j+1])+dp[i][ind-1]+dp[ind+1][j]
                    maxi=max(maxi,coin)
                dp[i][j]=maxi
        return dp[1][m-2]
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        m=len(nums)
        dp=[[0]*m for _ in range(m)]
        return self.func(nums,1,m-2,dp)