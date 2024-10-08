class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if nums[n-1]<target:
            return n
     

        start,end=0,n-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return start