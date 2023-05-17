# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        first_part = None
        f = head
        res = 0
        while head:
            if f:
                f = f.next.next
                first_part = ListNode(head.val, first_part)
            else:
                res = max(res, first_part.val + head.val)
                first_part = first_part.next
                
            head = head.next
        return res
        