from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.midorder(root,res)
        return res

    def midorder(self,Node: Optional[TreeNode],res:List[int]):
        if not Node:
            return None
        self.midorder(Node.left,res)
        res.append(Node.val)
        self.midorder(Node.right,res)