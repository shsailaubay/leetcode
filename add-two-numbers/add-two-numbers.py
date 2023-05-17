# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        curr_res_node = None
        buf = 0
        v1, v2 = l1, l2
        while v1 or v2:
            val = getattr(v1, 'val', 0) + getattr(v2, 'val', 0) + buf
            m, d = divmod(val, 10)
            buf = m
            if not result:
                result = ListNode(d)
                curr_res_node = result
            else:
                curr_res_node.next = ListNode(d)
                curr_res_node = curr_res_node.next
            v1, v2 = getattr(v1, 'next', None), getattr(v2, 'next', None)
        if buf:
            curr_res_node.next = ListNode(buf)
        return result
