from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        mono_st=deque()
        for i in range(len(nums)):
            if mono_st and mono_st[0]<=(i-k):
                mono_st.popleft()
            while mono_st and nums[mono_st[-1]]<nums[i]:
                mono_st.pop()
            mono_st.append(i)
            if i>=k-1:
                ans.append(nums[mono_st[0]])
            
        return ans