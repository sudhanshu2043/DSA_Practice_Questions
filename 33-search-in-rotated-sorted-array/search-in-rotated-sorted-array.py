class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        start,end=0,n-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            #it means the left part is sorted
            if nums[start]<=nums[mid]:
                if nums[start]<=target and nums[mid]>=target:
                    #target lies b/w start----mid
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid]<=target and nums[end]>=target:
                    start=mid+1
                else:
                    end=mid-1
        return -1