class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map={}
        ans=[]
        for i in range(len(nums)):
            if target-nums[i] in map:
                return [map[target-nums[i]],i]
            else:
                map[nums[i]]=i
        return []