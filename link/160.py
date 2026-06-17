from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l_a=1
        l_b=1
        na=headA
        nb=headB
        while na.next:
            l_a+=1
            na=na.next
        while nb.next:
            l_b+=1
            nb=nb.next
        diff=abs(l_a-l_b)
        if l_a>l_b:
            for i in range(diff):
                headA=headA.next
        else:
            for i in range(diff):
                headB=headB.next
        while headA:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None
