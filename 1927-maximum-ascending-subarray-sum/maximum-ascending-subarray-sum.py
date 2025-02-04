class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi = -float('inf')  # Initialize the maximum sum to the smallest possible value
        n = len(nums)
        for i in range(n):
            temp = nums[i]  # Start the current subarray sum with nums[i]
            if temp > maxi:
                maxi = temp  # Update maxi if the current element is larger
            # Extend the subarray as long as the next element is greater
            for j in range(i + 1, n):
                if nums[j] > nums[j - 1]:
                    temp += nums[j]
                    if temp > maxi:
                        maxi = temp  # Update maxi if the current subarray sum is larger
                else:
                    break  # Stop if the subarray is no longer ascending
        return maxi
        