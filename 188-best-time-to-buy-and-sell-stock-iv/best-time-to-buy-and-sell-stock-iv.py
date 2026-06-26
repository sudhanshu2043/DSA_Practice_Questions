class Solution:
    def get_max_profit(self,prices, n, ind, buy, cap, dp):
        # Base case: if we reach the end of the array or have no more capital left
        if ind == n or cap == 0:
            return 0

        # Check if the result is already calculated
        if dp[ind][buy][cap] != -1:
            return dp[ind][buy][cap]

        # Initialize profit
        profit = 0

        if buy == 0:  # We can buy the stock
            profit = max(
                0 + self.get_max_profit(prices, n, ind + 1, 0, cap, dp),
                -prices[ind] + self.get_max_profit(prices, n, ind + 1, 1, cap, dp)
            )

        if buy == 1:  # We can sell the stock
            profit = max(
                0 + self.get_max_profit(prices, n, ind + 1, 1, cap, dp),
                prices[ind] + self.get_max_profit(prices, n, ind + 1, 0, cap - 1, dp)
            )

        # Memoize the result and return
        dp[ind][buy][cap] = profit
        return profit
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp = [[[(-1) for _ in range(k + 1)] for _ in range(2)] for _ in range(n)]
        return self.get_max_profit(prices, n, 0, 0, k, dp)