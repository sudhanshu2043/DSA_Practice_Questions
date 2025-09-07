class Solution:
    def ispalindrome(self,s,start,end):
        while start<=end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True

    def fun(self,s,ind,ds,res):
        if ind==len(s):
            res.append(ds[:])
            return
        for i in range(ind,len(s)):
            if self.ispalindrome(s,ind,i):
                ds.append(s[ind:i+1])
                self.fun(s,i+1,ds,res)
                ds.pop()
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        ds=[]
        self.fun(s,0,ds,res)
        return res