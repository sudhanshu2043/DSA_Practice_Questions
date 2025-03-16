class Solution:
    def solve(self,arr):
        n = len(arr)
        prev = arr[0]
        prev2 = 0

        for i in range(1, n):
            pick = arr[i]
            if i > 1:
                pick += prev2
            nonPick = 0 + prev

            cur_i = max(pick, nonPick)
            prev2 = prev
            prev = cur_i

        return prev
        
    def rob(self, arr: List[int]) -> int:
        arr1 = []
        arr2 = []
        n=len(arr)
        if n == 1:
            return arr[0]

        for i in range(n):
            if i != 0:
                arr1.append(arr[i])
            if i != n - 1:
                arr2.append(arr[i])

        ans1 = self.solve(arr1)
        ans2 = self.solve(arr2)

        return max(ans1, ans2)