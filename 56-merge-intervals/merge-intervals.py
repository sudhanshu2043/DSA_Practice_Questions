class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals) # size of the array

        # sort the given intervals:
        intervals.sort()

        ans = []

        for i in range(n):
            # if the current interval does not
            # lie in the last interval:
            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            # if the current interval
            # lies in the last interval:
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans