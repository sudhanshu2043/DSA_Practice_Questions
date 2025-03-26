class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters) - 1
        ans = letters[0]  # Default to the first element if no greater letter is found
        
        while low <= high:
            mid = (low + high) // 2
            
            if letters[mid] > target:
                ans = letters[mid]  # Update the answer with a potential candidate
                high = mid - 1  # Move left to find a smaller valid character
            else:
                low = mid + 1  # Move right if mid is less than or equal to target
        
        return ans