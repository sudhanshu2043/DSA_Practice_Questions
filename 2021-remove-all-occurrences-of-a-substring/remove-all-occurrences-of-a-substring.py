class Solution:
    def compute_lps(self,pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]  # fallback
                else:
                    lps[i] = 0
                    i += 1
        return lps
    def kmp_search(self,text, pattern):
        lps = self.compute_lps(pattern)
        i = j = 0  # i -> text index, j -> pattern index
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            if j == len(pattern):
                return i-j
                j = lps[j - 1]  # continue searching
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    # def removeOccurrences(self, s: str, part: str) -> str:
    #     while True:
    #         # Use your KMP function to find the index of the leftmost occurrence.
    #         idx = self.kmp_search(s, part)
            
    #         # If kmp_search returns -1, it means 'part' is no longer in 's'.
    #         if idx == -1:
    #             break
            
    #         # If 'part' was found, reconstruct 's' without that occurrence.
    #         s = s[:idx] + s[idx + len(part):]
            
    #     return s
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)
        
        # Iterate through each character in the input string s
        for char in s:
            # 1. Push the current character onto the stack
            stack.append(char)
            # 2. Check if the end of the stack matches 'part'
            if len(stack) >= part_len and "".join(stack[-part_len:]) == part:
                # 3. If it matches, pop the 'part' from the stack
                # We can do this by repeatedly calling pop() or with a single slice deletion
                del stack[-part_len:]
                
        # Join the characters in the stack to form the final result
        return "".join(stack)
