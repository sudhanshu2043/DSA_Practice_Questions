class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        st=[]
        for i in range(2*n):
            num = nums[i % n]  # Get the current element, modulo to handle circular
            while st and nums[st[-1]] < num:
                ans[st.pop()] = num
            if i < n:
                st.append(i)

        return ans