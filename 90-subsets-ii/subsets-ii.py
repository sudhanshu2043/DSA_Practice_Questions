class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ds=[]
        def generate(ind,ans,ds):
            ans.append(ds[:])
            for i in range(ind,len(nums)):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                ds.append(nums[i])
                generate(i+1,ans,ds)
                ds.pop()
        nums.sort()
        generate(0,ans,ds)
        return ans