class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp=[]
        for i in range(m):
            temp.append(nums1[i])
        for j in range(n):
            temp.append(nums2[j])
        temp.sort()
        for i in range(m+n):
            nums1[i]=temp[i]
        