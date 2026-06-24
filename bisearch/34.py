from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(x):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= x:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        left = lower_bound(target)
        right = lower_bound(target + 1) - 1

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        return [left, right]
