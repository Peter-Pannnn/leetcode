from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        cur_sum = 0
        ans = 0

        for num in nums:
            cur_sum += num

            need = cur_sum - k
            ans += prefix_count.get(need, 0)

            prefix_count[cur_sum] = prefix_count.get(cur_sum, 0) + 1

        return ans