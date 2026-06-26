from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[0]: First Buy, dp[1]: First Sell, dp[2]: Second Buy, dp[3]: Second Sell
        # Base Case: Out of bounds day (day n) yields 0 profit across all states
        dp = [0] * 4
        
        # Loop backwards through days
        for price in reversed(prices):
            # We loop backwards through states (from 3 down to 0) so we don't 
            # overwrite values from 'tomorrow' that are needed for 'today'
            
            # State 3: Second Sell (Odd state -> Sell)
            dp[3] = max(price + 0, dp[3]) # selling gives cash, transaction ends (profit 0 after)
            
            # State 2: Second Buy (Even state -> Buy)
            dp[2] = max(-price + dp[3], dp[2]) # buying costs cash, transitions to State 3
            
            # State 1: First Sell (Odd state -> Sell)
            dp[1] = max(price + dp[2], dp[1]) # selling gives cash, transitions to State 2
            
            # State 0: First Buy (Even state -> Buy)
            dp[0] = max(-price + dp[1], dp[0]) # buying costs cash, transitions to State 1
            
        # Ultimately, we want the max profit starting from the very first action (First Buy)
        return dp[0]