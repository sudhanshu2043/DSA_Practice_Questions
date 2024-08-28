class Solution:
    def solve(self,nums,k):
        l,r=0,0
        cnt=0
        mpp={}
        while r < len(nums):
            if nums[r] in mpp:
                mpp[nums[r]]+=1
            else:
                mpp[nums[r]]=1
            while len(mpp)>k:
                mpp[nums[l]]-=1
                if mpp[nums[l]]==0:
                    del mpp[nums[l]]
                l+=1
            cnt+=(r-l+1)
            r+=1
        return cnt
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.solve(nums,k)-self.solve(nums,k-1)
        