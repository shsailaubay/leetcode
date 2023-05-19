# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ln = 0
        prev = head
        while prev:
            prev = prev.next
            ln += 1
        if ln == n:
            return head.next
        prev = head
        for i in range(0, ln - n - 1):
            prev = prev.next
        prev.next = prev.next.next
        return head
