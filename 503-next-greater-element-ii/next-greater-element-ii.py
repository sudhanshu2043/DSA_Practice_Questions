class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n  # Initialize all results as -1
        st = []  # Stack to keep track of indices

        # Traverse the array twice to handle the circular nature
        for i in range(2 * n):
            num = nums[i % n]  # Get the current element, modulo to handle circular
            while st and nums[st[-1]] < num:
                ans[st.pop()] = num
            if i < n:
                st.append(i)

        return ans