# Definition for a binary tree node.
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(0, len(nums) - 1, nums)
    
    def build(self, left, right, nums):
        if left > right:
            return None

        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        root.left = self.build(left, mid - 1, nums)
        root.right = self.build(mid + 1, right, nums)

        return root
