class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        for i in details:
            age=i[11:13]
            if int(age)>60:
                ans+=1
        return ans
