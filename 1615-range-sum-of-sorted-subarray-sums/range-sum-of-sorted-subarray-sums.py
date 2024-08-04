class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        temp = []
        
        # Generate all subarray sums
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                temp.append(sum)
        
        # Sort the subarray sums
        temp.sort()
        
        # Adjust indices from 1-based to 0-based
        left -= 1
        right -= 1
        
        # Calculate the sum from index left to right (inclusive)
        sumAns = 0
        for i in range(left, right + 1):
            sumAns += temp[i]
        
        # Return the result modulo 10^9 + 7
        return sumAns % (10**9 + 7)