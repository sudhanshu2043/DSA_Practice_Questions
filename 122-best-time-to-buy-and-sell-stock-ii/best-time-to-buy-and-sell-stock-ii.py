class Solution:
    def func(self,prices,dp):
        n=len(prices)
        curr=[0]*2
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                profit=0
                if buy:
                    # Option 1: Buy today -> deduct money, next state becomes 'cannot buy' (0)
                    # Option 2: Skip today -> money stays same, next state stays 'can buy' (1)
                    profit=max(-prices[ind]+dp[0],dp[1])
                else:
                    # Option 1: Sell today -> gain money, next state becomes 'can buy' (1)
                    # Option 2: Skip today -> money stays same, next state stays 'cannot buy' (0)
                    profit=max(prices[ind]+dp[1],dp[0])
                curr[buy]= profit
            dp=curr
        return dp[1]
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[0]*2 
        return self.func(prices,dp)