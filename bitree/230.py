# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.num=0
        self.res=[]
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root)
        return self.res[k-1]
    def inorder(self,node):
        if not node:
            return
        self.inorder(node.left)
        self.res.append(node.val)
        self.inorder(node.right)


