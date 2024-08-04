class Solution:
    def square(self,n):
        ans=0
        while n>0:
            remainder=n%10
            ans+=(remainder*remainder)
            n=n//10
        return ans
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        clock = True
        while slow != fast or clock:
            if clock:
                clock = False
            slow = self.square(slow)
            fast = self.square(self.square(fast))
        return slow == 1