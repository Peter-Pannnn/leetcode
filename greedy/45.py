from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        cur_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == cur_end:
                steps += 1
                cur_end = farthest

        return steps
