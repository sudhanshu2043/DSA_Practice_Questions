class Solution:
    # Recursive Code TC-O(3^N) Sc-0(N)
    def solve(self,s,ind,cnt):
        if cnt<0: return False
        if ind==len(s): return cnt==0
        if s[ind]=='(':
            return self.solve(s,ind+1,cnt+1)
        if s[ind]==')':
            return self.solve(s,ind+1,cnt-1)
        return self.solve(s,ind+1,cnt+1) or self.solve(s,ind+1,cnt-1) or self.solve(s,ind+1,cnt)
    def checkValidString(self, s: str) -> bool:
        mini,maxi=0,0
        for i in range(len(s)):
            if s[i]=='(':
                mini+=1
                maxi+=1
            elif s[i]==')':
                mini-=1
                maxi-=1
            else:
                mini-=1
                maxi+=1
            if mini<0: mini=0
            if maxi<0: return False
        return mini==0