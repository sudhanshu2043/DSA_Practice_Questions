class Solution:
    def solve(self,s,i):
        n = len(s)
        # Base case: if the pointer has reached or crossed the middle, it's a palindrome
        if i >= n // 2:
            return True
        # Check characters from the start and end moving towards the center
        if s[i] != s[n - i - 1]:
            return False
        # Recursive call for the next pair of characters
        return self.solve(s, i + 1)
    
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        return self.solve(filtered_s, 0)
   