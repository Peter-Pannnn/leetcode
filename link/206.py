# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None       # 相当于前一个节点，初始时它为空
        curr = head       # 当前节点
        
        while curr:
            temp_node = curr.next  # 暂存下一个节点
            curr.next = prev       # 当前节点反转指向前一个节点
            prev = curr            # prev 往后挪一步
            curr = temp_node       # curr 往后挪一步
            
        return prev       # 遍历结束时，curr 为空，prev 正好指向新的头节