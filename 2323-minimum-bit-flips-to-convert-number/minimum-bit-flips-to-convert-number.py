class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=start^goal
        cnt=0
        while ans!=0:
            ans=ans&(ans-1)
            cnt+=1
        return cnt