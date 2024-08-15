class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten,twenty=0,0,0
        for i in range(len(bills)):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five:
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                if five and ten:
                    five-=1
                    ten-=1
                    twenty+=1
                elif five>=3:
                    five-=3
                    twenty+=1
                else:
                    return False
        return True