class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        temp = []
        temp.append(nums[0])
        # Iterate on the elements of the array
        for i in range(1, n):
            # If the current element can be added to the subsequence
            if nums[i] > temp[-1]:
                temp.append(nums[i]) 
            # Otherwise
            else:
                # Index at which the current element must be placed
                ind = self.lower_bound(temp, nums[i])
                # Place the current element in the subsequence
                temp[ind] = nums[i]
        # Return the length of temporary subsequence created so far
        return len(temp)
    # Binary search to find the index of the smallest element >= target
    def lower_bound(self, temp, target):
        left, right = 0, len(temp) - 1
        while left <= right:
            mid = (left + right) // 2
            if temp[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left