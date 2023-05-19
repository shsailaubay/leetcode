# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        ln = 1
        i = 0
        prev = head
        while fast.next:
            fast = fast.next
            ln += 1
        if i == ln - n:
            return prev.next
        while True:
            if ln - i - 1 == n:
                break
            prev = prev.next
            i += 1
        prev.next = prev.next.next
        return head
