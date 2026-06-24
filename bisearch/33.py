from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # 1. 先找旋转点 k，也就是最小值的位置
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        k = left

        # 2. 根据 target 判断应该在哪一段二分
        if nums[k] <= target <= nums[n - 1]:
            left = k
            right = n - 1
        else:
            left = 0
            right = k - 1

        # 3. 普通二分查找
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
