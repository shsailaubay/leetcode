# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        f = head
        res = 0
        stack = []
        while head:
            if f:
                f = f.next.next
                stack.append(head.val)
            else:
                res = max(res, stack.pop() + head.val)
            head = head.next
        return res
        