from math import gcd
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans=[]
        for j in range(2, n+1):
            for i in range(1, j):
                if gcd(i, j) == 1:
                    ans.append(f"{i}/{j}")
        return ans