import math
class Solution:
    def calculate(self,nums,mid):
        sum=0
        for i in nums:
            sum+=math.ceil(i/mid)
        return sum
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        if n > threshold:
            return -1
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            divisor=self.calculate(nums,mid)
            if divisor<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low