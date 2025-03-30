class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans=-1
        low,high=0,len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            # check left part is sorted or not
            if nums[low]<=nums[mid]:
                if nums[mid]>target and nums[low]<=target:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target and nums[high]>=target:
                    low=mid+1
                else:
                    high=mid-1
        return ans