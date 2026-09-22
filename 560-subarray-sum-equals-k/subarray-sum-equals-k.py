class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:

        prefix_sum = 0
        count = 0

        prefix_map = {0: 1}

        for i in range(len(arr)):

            prefix_sum += arr[i]

            needed = prefix_sum - k

            if needed in prefix_map:
                count += prefix_map[needed]

            # Store/update frequency
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count