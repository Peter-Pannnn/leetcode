from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    dummy = ListNode()
    cur = dummy

    for value in values:
        cur.next = ListNode(value)
        cur = cur.next

    return dummy.next


def print_linked_list(head):
    values = []
    cur = head

    while cur:
        values.append(str(cur.val))
        cur = cur.next

    print(" -> ".join(values))


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre = None
        cur = slow
        while cur:
            temp_node = cur.next  # 暂存下一个节点
            cur.next = pre        # 当前节点反转指向前一个节点
            pre = cur             # pre 往后挪一步
            cur = temp_node       # cur 往后挪一步


        p1 = head
        p2 = pre
        print("反转后链表")
        print_linked_list(p1)

        print_linked_list(p2)
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 2, 1])

    print("原始链表：")
    print_linked_list(head)

    s = Solution()
    print("是否为回文链表：", s.isPalindrome(head))
