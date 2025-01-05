class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        for i in range(len(intervals)):
            first=intervals[i][0]
            last=intervals[i][1]

            if ans and last<=ans[-1][1]:
                continue

            for j in range(i+1,len(intervals)):
                if last>=intervals[j][0]:
                    last=max(last,intervals[j][1])
                else:
                    break
            
            ans.append([first,last])
        return ans