
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num
            j = seen.get(need, -1)
            if j != -1:
                return [j, i]
            seen[num] = i

        return []
