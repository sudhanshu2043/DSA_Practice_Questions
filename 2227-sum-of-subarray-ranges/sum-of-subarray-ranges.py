class Solution:
    def sumSubarrayMinimums(self, nums):
        n = len(nums)
        min_contribution = 0
        stack = []
        
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] >= nums[i]):
                j = stack.pop()
                k = stack[-1] if stack else -1
                min_contribution += nums[j] * (i - j) * (j - k)
            stack.append(i)
        
        return min_contribution

    def sumSubarrayMaximums(self, nums):
        n = len(nums)
        max_contribution = 0
        stack = []
        
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] <= nums[i]):
                j = stack.pop()
                k = stack[-1] if stack else -1
                max_contribution += nums[j] * (i - j) * (j - k)
            stack.append(i)
        
        return max_contribution
    def subArrayRanges(self, nums: List[int]) -> int:
        max_sum = self.sumSubarrayMaximums(nums)
        min_sum = self.sumSubarrayMinimums(nums)
        
        # The sum of all ranges will be the difference between max_sum and min_sum
        return max_sum - min_sum