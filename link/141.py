# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast == slow:
                return True
        return False
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast == slow:
                p1=head
                p2=slow
                while p1!=p2:
                    p1=p1.next
                    p2=p2.next

                return p1
        return None
