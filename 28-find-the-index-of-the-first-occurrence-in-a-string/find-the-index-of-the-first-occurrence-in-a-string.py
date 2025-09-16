class Solution:
    def zArrFn(self,s):
        n=len(s)
        arr=[0]*n
        i=1
        cnt=0
        while i<n:
            j=0
            k=i
            while k<n and s[k]==s[j]:
                k+=1
                j+=1
            else:
                arr[i]=j
            i+=1
        return arr
    def strStr(self, haystack: str, needle: str) -> int:
        concat=needle+'$'+haystack
        m=len(needle)
        zArr=self.zArrFn(concat)
        i=m+1
        while i < len(concat):
            if zArr[i]==m:
                break
            i+=1
        return i-m-1 if i<len(concat) else -1