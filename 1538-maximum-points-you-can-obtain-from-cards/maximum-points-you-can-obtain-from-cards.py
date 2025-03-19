class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxSum=0
        lsum=0
        for i in range(k):
            lsum+=cardPoints[i]
        maxSum=lsum
        rindex=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            lsum+=cardPoints[rindex]
            maxSum=max(maxSum,lsum)
            rindex-=1
        return maxSum