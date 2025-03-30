class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=float('inf')
        low,high=0,len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            ans=min(nums[mid],ans)
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                high=mid-1
        return ans