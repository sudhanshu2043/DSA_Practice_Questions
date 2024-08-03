class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=None
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                cnt=1
                candidate=nums[i]
            elif candidate==nums[i]:
                cnt+=1
            else:
                cnt-=1
                
        cnt=0
        for i in range(len(nums)):
            if candidate==nums[i]:
                cnt+=1

        if cnt>=len(nums)//2:
            return candidate