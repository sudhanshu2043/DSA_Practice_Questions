class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def func(self, s, dp):
        for i in range(len(s)-1,-1,-1):
            minCost = 1e9
            temp = ""
            for j in range(i, len(s)):
                temp += s[j]
                if self.isPalindrome(temp):
                    # Count blocks instead of cuts to avoid boundary edge cases
                    cost = 1 + dp[j + 1]
                    minCost = min(minCost, cost)
                    
            dp[i] = minCost
        return dp[0]

    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        # Subtract 1 at the end because cuts = total_parts - 1
        return self.func( s, dp) - 1