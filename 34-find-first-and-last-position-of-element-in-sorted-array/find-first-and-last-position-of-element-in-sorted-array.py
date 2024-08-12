class Solution:
    def firstPosition(self,nums,target):
        ans=-1
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                ans=mid
                end=mid-1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return ans
    def lastPosition(self,nums,target):
        ans=-1
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                ans=mid
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=self.firstPosition(nums,target)
        last=self.lastPosition(nums,target)
        return [first,last]