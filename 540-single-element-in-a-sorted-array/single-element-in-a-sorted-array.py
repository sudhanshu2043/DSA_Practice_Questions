class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor=0
        for i in range(len(nums)):
            xor=xor^nums[i]
        return xor