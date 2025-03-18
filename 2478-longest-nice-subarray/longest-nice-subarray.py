class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        andd = 0
        left = 0  # This will track the left boundary of the subarray
        
        for right in range(len(nums)):
            # Update the andd with the current number
            while andd & nums[right] != 0:
                # If the AND isn't zero, shrink the window from the left
                andd ^= nums[left]
                left += 1
            
            # Add the current number to the AND value
            andd |= nums[right]
            
            # Calculate the length of the current nice subarray
            ans = max(ans, right - left + 1)
        
        return ans
