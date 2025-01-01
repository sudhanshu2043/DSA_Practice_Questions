class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxProfit=0
        for i in range(1,len(prices)):
            mini=min(mini,prices[i])
            maxProfit=max(maxProfit,prices[i]-mini)
        return maxProfit