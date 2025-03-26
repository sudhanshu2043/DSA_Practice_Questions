class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low,high=0,len(letters)-1
        if ord(target)>=ord(letters[high]):
            return letters[0]
        ans=0
        while low<=high:
            mid=low+(high-low)//2
            if ord(letters[mid])==ord(target):
                while ord(letters[mid+1])==ord(target):
                    mid+=1
                return letters[mid+1]
            elif ord(letters[mid])<ord(target):
                ans=mid+1
                low=mid+1
            else:
                high=mid-1

        return letters[ans]