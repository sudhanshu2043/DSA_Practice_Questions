class Solution:
    def func(self, s, p, i, j,dp):
        # Base Case 1: Both string and pattern are completely exhausted
        if i < 0 and j < 0: 
            return True
        
        # Base Case 2: Pattern is exhausted, but the string still has characters
        if j < 0 and i >= 0: 
            return False
            
        # Base Case 3: String is exhausted, but the pattern still has characters
        # This is only True if every remaining character in the pattern is a '*'
        if i < 0 and j >= 0:
            for k in range(j + 1):
                if p[k] != '*':
                    return False
            return True
        if dp[i][j]!=None: return dp[i][j]
        # Matching Logic (p contains the wildcards)
        if s[i] == p[j] or p[j] == '?':
            dp[i][j]= self.func(s, p, i - 1, j - 1,dp)
            return dp[i][j]
        elif p[j] == '*':
            # Two choices when encountering '*':
            # 1. Treat '*' as an empty string (0 characters) -> move pattern pointer (j - 1)
            # 2. Treat '*' as matching today's character -> move string pointer (i - 1)
            dp[i][j]= self.func(s, p, i, j - 1,dp) or self.func(s, p, i - 1, j,dp)
            return dp[i][j]
        dp[i][j]= False
        return dp[i][j]

    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp=[[None]*m for _ in range(n)]
        return self.func(s, p, n - 1, m - 1,dp)