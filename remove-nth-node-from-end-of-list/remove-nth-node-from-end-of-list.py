# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        ln = 0
        i = 0
        prev = head
        while slow:
            if fast:
                for i in [0,1]:
                    if fast:
                        fast = fast.next
                        ln += 1

            if not fast:
                if ln - i < n:
                    break
                elif ln - i + 1 == n:
                    prev.next = prev.next.next
                    return head
            prev = slow
            slow = slow.next
            i += 1
        i = 0
        prev = head
        if i == ln - n:
            return prev.next
        while True:
            if ln - i - 1 == n:
                break
            prev = prev.next
            i += 1
        prev.next = prev.next.next
        return head
