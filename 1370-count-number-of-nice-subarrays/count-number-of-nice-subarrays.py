class Solution:
    def atMost(self,nums,k):
        l,r=0,0
        maxi=0
        nice=0
        if k<0:
            return 0
        while r<len(nums):
            if nums[r]%2==1:
                maxi+=1
            while maxi>k:
                if nums[l]%2==1:
                    maxi-=1
                l+=1
            nice+=(r-l+1)
            r+=1
        return nice
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums,k)-self.atMost(nums,k-1)