class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        next_greater = {}
        
        for num in reversed(nums2):
            while s and s[-1] <= num:
                s.pop()
            
            # If stack is empty, there is no greater element
            if s:
                next_greater[num] = s[-1]
            else:
                next_greater[num] = -1
            
            # Push the current element onto the stack
            s.append(num)
        
        # Prepare the result for nums1 based on the computed next greater elements
        return [next_greater[num] for num in nums1]