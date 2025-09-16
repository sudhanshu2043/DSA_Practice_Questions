class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mpp={}
        for i in range(len(s)):
            ch=s[i]
            if ch in mpp:
                mpp[ch]+=1
            else:
                mpp[ch]=1
        for i in range(len(t)):
            ch=t[i]
            if ch in mpp:
                mpp[ch]-=1
                if mpp[ch]==0:
                    del mpp[ch]
            else:
                return False
        return True