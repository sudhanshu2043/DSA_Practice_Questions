class Solution:
    def get_sum(self,mid, index, n):
        # Left side (from index-1 to 0)
        if mid > index:
            left_sum = (mid + mid - index) * (index + 1) // 2
        else:
            left_sum = (mid + 1) * mid // 2 + (index - mid + 1)

        # Right side (from index+1 to n-1)
        right_len = n - index - 1
        if mid > right_len:
            right_sum = (mid + mid - right_len) * (right_len + 1) // 2
        else:
            right_sum = (mid + 1) * mid // 2 + (right_len - mid + 1)

        total = left_sum + right_sum - mid  # subtract mid since it's counted twice
        return total

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        low, high = 1, maxSum

        while low <= high:
            mid = (low + high) // 2
            total = self.get_sum(mid, index, n)

            if total <= maxSum:
                low = mid + 1
            else:
                high = mid - 1

        return high