class Solution:
    def atMost(self,nums,goal):
        if goal<0:
            return 0
        l,r=0,0
        sum=0
        ans=0
        while r<len(nums):
            sum+=nums[r]
            while sum>goal:
                sum-=nums[l]
                l+=1
            ans+=(r-l+1)
            r+=1
        return ans
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)