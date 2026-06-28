class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        # 1. Sort the cuts so independent subproblems can be formed
        cuts.sort()
        
        # 2. Append 0 and n to represent the boundaries of the stick
        cuts = [0] + cuts + [n]
        m = len(cuts)
        
        # 3. Create a 2D DP array initialized to 0
        # Base cases where i > j are implicitly handled as 0
        dp = [[0] * m for _ in range(m)]
        
        # 4. Nested loops to solve from smallest subproblems to largest
        # i moves backwards (from the last actual cut down to 1)
        for i in range(m - 2, 0, -1):
            # j moves forward (from i up to the last actual cut)
            for j in range(i, m - 1):
                
                mini = float('inf')
                # The length of the current stick we are cutting
                current_stick_length = cuts[j + 1] - cuts[i - 1]
                
                # Try making a cut at every available independent index 'ind'
                for ind in range(i, j + 1):
                    cost = current_stick_length + dp[i][ind - 1] + dp[ind + 1][j]
                    if cost < mini:
                        mini = cost
                        
                dp[i][j] = mini
                
        # The answer for the entire stick spanning from cut index 1 to m-2
        return dp[1][m - 2]