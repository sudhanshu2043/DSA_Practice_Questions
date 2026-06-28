class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
            
        # Initialize a 2D table with 0
        dp = [[0] * n for _ in range(n)]
        
        self.max_len = 1
        self.start_idx = 0
        
        # Base Case: All single-character substrings are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # FIX 2: Iterate through substring lengths starting from 2 up to n
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                
                # Check for length 2 strings (no inner substring to check)
                if s[i] == s[j] and L == 2:
                    dp[i][j] = 1
                    # FIX 1: Explicitly use self. to update class trackers
                    self.max_len = L
                    self.start_idx = i
                    
                # Check for length > 2 strings (inner substring must be a palindrome)
                elif s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                    # FIX 1: Explicitly use self. to update class trackers
                    self.max_len = L
                    self.start_idx = i
                
        # Slice and return the longest palindromic substring discovered
        return s[self.start_idx : self.start_idx + self.max_len]