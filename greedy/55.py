from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest=0
        length=len(nums)
        for i in range(length):
            if i>farthest:
                return False
            farthest=max(farthest,i+nums[i])
            if farthest>=length-1:
                return True
        return True