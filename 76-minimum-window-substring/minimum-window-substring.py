class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = [0] * 256
        ans = float('inf')  # length of the answer
        start = 0  # starting index of the answer
        count = 0
        # Creating the frequency map for string t
        for char in t:
            if m[ord(char)] == 0:
                count += 1
            m[ord(char)] += 1
        i = 0
        j = 0
        # Traversing the window
        while j < len(s):
            # Decrease the frequency of the current character
            m[ord(s[j])] -= 1
            if m[ord(s[j])] == 0:
                count -= 1

            # Check if we have a valid window
            if count == 0:
                while count == 0:
                    # Update the answer if we found a smaller window
                    if ans > j - i + 1:
                        ans = j - i + 1
                        start = i
                    
                    # Sliding the left pointer i to reduce the window size
                    m[ord(s[i])] += 1
                    if m[ord(s[i])] > 0:
                        count += 1
                    i += 1

            j += 1

        # Return the substring if found, else an empty string
        return s[start:start + ans] if ans != float('inf') else ""
