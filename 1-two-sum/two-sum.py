class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp={}
        for i in range(len(nums)):
            temp[nums[i]]=i
        for i in range(len(nums)):
            more_needed=target-nums[i]
            if more_needed in temp.keys() and i!=temp.get(more_needed):
                return [i,temp.get(more_needed)]
        return [-1,-1]