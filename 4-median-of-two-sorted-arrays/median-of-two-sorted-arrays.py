class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp=[]
        for i in nums1:
            temp.append(i)
        for i in nums2:
            temp.append(i)
        temp.sort()
        if len(temp)%2==1:
            return temp[len(temp)//2]
        else:
            return (temp[len(temp)//2]+temp[(len(temp)//2)-1])/2