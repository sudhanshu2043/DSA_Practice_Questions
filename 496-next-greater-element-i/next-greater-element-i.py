class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        nxt_greater={}
        for num in reversed(nums2):
            while stack and stack[-1]<=num:
                stack.pop()
            if len(stack)==0:
                nxt_greater[num]=-1
            else:
                nxt_greater[num]=stack[-1]
            stack.append(num)
        ans=[nxt_greater[x] for x in nums1]
        return ans