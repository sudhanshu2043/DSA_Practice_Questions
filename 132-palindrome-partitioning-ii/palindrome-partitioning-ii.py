class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def func(self, i, s, dp):
        if i == len(s): 
            return 0
        
        if dp[i] != -1:
            return dp[i]
            
        minCost = 1e9
        temp = ""
        for j in range(i, len(s)):
            temp += s[j]
            if self.isPalindrome(temp):
                # Count blocks instead of cuts to avoid boundary edge cases
                cost = 1 + self.func(j + 1, s, dp)
                minCost = min(minCost, cost)
                
        dp[i] = minCost
        return dp[i]

    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        # Subtract 1 at the end because cuts = total_parts - 1
        return self.func(0, s, dp) - 1