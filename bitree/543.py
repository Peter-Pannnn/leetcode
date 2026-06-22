# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.res
    def depth(self,Node:Optional[TreeNode]):
        if not Node:
            return 0
        left=self.depth(Node.left)
        right=self.depth(Node.right)
        self.res=max(left+right,self.res)
        return max(left,right)+1