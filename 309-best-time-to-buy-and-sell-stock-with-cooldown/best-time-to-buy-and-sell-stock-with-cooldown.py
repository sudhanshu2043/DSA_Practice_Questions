class Solution:
    def func(self,prices,dp):
        n=len(prices)
        dp[n][0],dp[n][1]=0,0
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                profit=0
                if buy:
                    # Option 1: Buy today -> deduct money, next state becomes 'cannot buy' (0)
                    # Option 2: Skip today -> money stays same, next state stays 'can buy' (1)
                    profit=max(-prices[ind]+dp[ind+1][0],dp[ind+1][1])
                else:
                    # Option 1: Sell today -> gain money, next state becomes 'can buy' (1)
                    # Option 2: Skip today -> money stays same, next state stays 'cannot buy' (0)
                    profit=max(prices[ind]+dp[ind+2][1],dp[ind+1][0])
                dp[ind][buy]= profit
        return dp[0][1]
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(n+2)]
        return self.func(prices,dp)
        