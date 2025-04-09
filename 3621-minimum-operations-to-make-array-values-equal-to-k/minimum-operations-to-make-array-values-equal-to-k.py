class Solution(object):
    def minOperations(self, nums, k):
        mini = min(nums)
        if mini < k:
            return -1
        st = set(nums)
        return len(st) - (mini == k)