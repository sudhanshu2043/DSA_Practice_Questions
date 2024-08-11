class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def generate(ind):
            if ind==len(nums):
                ans.append(nums[:])
                return
            for i in range(ind,len(nums)):
                nums[ind],nums[i]=nums[i],nums[ind]
                generate(ind+1)
                nums[ind],nums[i]=nums[i],nums[ind]
        generate(0)
        return ans