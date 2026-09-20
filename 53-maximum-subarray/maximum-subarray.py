class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum=0
        ans=float('-inf')
        for i in range(len(nums)):
            sum+=nums[i]
            ans=max(ans,sum)
            if sum<0:
                sum=0
        return ans