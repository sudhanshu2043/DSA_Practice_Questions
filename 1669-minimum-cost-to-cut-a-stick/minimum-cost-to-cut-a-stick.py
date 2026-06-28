class Solution:
    def func(self, i, j, cuts, dp):
        if i > j: 
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
            
        mini = 1e9
        # The cost to cut the current stick segment
        current_stick_length = cuts[j + 1] - cuts[i - 1]
        
        for ind in range(i, j + 1): # j is inclusive
            cost = current_stick_length + self.func(i, ind - 1, cuts, dp) + self.func(ind + 1, j, cuts, dp)
            mini = min(cost, mini)
            
        dp[i][j] = mini
        return dp[i][j]

    def minCost(self, n: int, cuts: list[int]) -> int:
        # 1. MUST SORT the cuts first
        cuts.sort()
        
        # 2. Pad with 0 and n to easily grab stick lengths
        cuts = [0] + cuts + [n]
        c = len(cuts)
        
        # dp array size based on padded cuts length
        dp = [[-1] * c for _ in range(c)]
        
        # i starts at 1, j ends at len(cuts) - 2 (the last actual cut index)
        return self.func(1, len(cuts) - 2, cuts, dp)