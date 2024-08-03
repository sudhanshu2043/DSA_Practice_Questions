class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1,ele2=None,None
        cnt1,cnt2=0,0
        ans=[]
        for i in range(len(nums)):
            if cnt1 == 0 and ele2 != nums[i]:
                cnt1 = 1
                ele1 = nums[i]
            elif cnt2 == 0 and ele1 != nums[i]:
                cnt2 = 1
                ele2 = nums[i]
            elif nums[i] == ele1:
                cnt1 += 1
            elif nums[i] == ele2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1,cnt2=0,0
        for i in range(len(nums)):
            if ele1==nums[i]:
                cnt1+=1
            if ele2==nums[i]:
                cnt2+=1
        mini=(len(nums)//3)+1
        if cnt1>=mini:
            ans.append(ele1)
        if cnt2>=mini:
            ans.append(ele2)
        return ans