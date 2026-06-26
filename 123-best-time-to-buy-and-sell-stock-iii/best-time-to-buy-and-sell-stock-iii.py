from typing import List

class Solution:
    def func(self, prices, dp):
        n = len(prices)
        
        # Loop backwards from day n-1 down to 0
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                # FIX 1: Start from 1 to avoid cap-1 becoming -1
                for cap in range(1, 3): 
                    if buy:
                        dp[ind][buy][cap] = max(-prices[ind] + dp[ind + 1][0][cap], 
                                                 dp[ind + 1][1][cap])
                    else:
                        dp[ind][buy][cap] = max(prices[ind] + dp[ind + 1][1][cap - 1], 
                                                 dp[ind + 1][0][cap])
                                    
        # FIX 3: Return the specific starting state: Day 0, Can Buy, 2 Transactions left
        return dp[0][1][2]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        # FIX 2: Initialize with 0 instead of -1. 
        # This automatically sets up the base cases for ind == n and cap == 0.
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        
        # No need to pass starting values as parameters anymore
        return self.func(prices, dp)