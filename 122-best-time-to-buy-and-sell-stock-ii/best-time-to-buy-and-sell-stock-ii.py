class Solution:
    def func(self,ind,prices,buy,dp):
        if len(prices)==ind:
            return 0
        if dp[ind][buy]!=-1: return dp[ind][buy]
        profit=0
        if buy:
            # Option 1: Buy today -> deduct money, next state becomes 'cannot buy' (0)
            # Option 2: Skip today -> money stays same, next state stays 'can buy' (1)
            profit=max(-prices[ind]+self.func(ind+1,prices,0,dp),self.func(ind+1,prices,1,dp))
        else:
            # Option 1: Sell today -> gain money, next state becomes 'can buy' (1)
            # Option 2: Skip today -> money stays same, next state stays 'cannot buy' (0)
            profit=max(prices[ind]+self.func(ind+1,prices,1,dp),self.func(ind+1,prices,0,dp))
        dp[ind][buy]= profit
        return dp[ind][buy]
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        return self.func(0,prices,1,dp)