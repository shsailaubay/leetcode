# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        ln = 0
        prev = head
        while fast:
            fast = fast.next
            ln += 1
        if ln == n:
            return prev.next
        for i in range(0, ln - n - 1):
            prev = prev.next
        prev.next = prev.next.next
        return head
