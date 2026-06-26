from typing import List

class Solution:
    def func(self, prices, dp, ind, buy, cap):
        # Base Case 1: Out of days
        if ind == len(prices): 
            return 0
        # Base Case 2: No transactions left allowed
        if cap == 0: 
            return 0
            
        # Check if we already calculated this state
        if dp[ind][buy][cap] != -1: 
            return dp[ind][buy][cap]
        
        if buy:
            # Option 1: Buy today -> cap stays same, next state cannot buy (0)
            # Option 2: Skip today -> cap stays same, next state can buy (1)
            dp[ind][buy][cap] = max(-prices[ind] + self.func(prices, dp, ind + 1, 0, cap),
                                    self.func(prices, dp, ind + 1, 1, cap))
        else:
            # Option 1: Sell today -> cap decreases by 1, next state can buy (1)
            # Option 2: Skip today -> cap stays same, next state cannot buy (0)
            dp[ind][buy][cap] = max(prices[ind] + self.func(prices, dp, ind + 1, 1, cap - 1),
                                    self.func(prices, dp, ind + 1, 0, cap))
                                    
        return dp[ind][buy][cap]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # Dimensions: [ind from 0 to n][buy from 0 to 1][cap from 0 to 2]
        # Size: (n + 1) x 2 x 3
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]
        # Start on Day 0, allowed to buy (1), with 2 transactions left
        return self.func(prices, dp, 0, 1, 2)