class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ans=1
        while True:
            temp=ans*ans
            if temp==num: return True
            elif temp>num: break
            else:
                ans+=1
        return False