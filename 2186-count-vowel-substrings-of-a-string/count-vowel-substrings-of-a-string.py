from collections import defaultdict
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = 0
        start = left = 0
        freq = defaultdict(int)

        for right in range(len(word)):
            if word[right] not in vowels:
                freq.clear()
                start = left = right + 1  # Reset pointers
                continue
            freq[word[right]] += 1  # Add vowel to hashmap
            while len(freq) == 5:  # If all vowels are present
                freq[word[left]] -= 1
                if freq[word[left]] == 0:
                    del freq[word[left]]
                left += 1  # Shrink the window
            ans += left - start  # Count valid substrings
        return ans