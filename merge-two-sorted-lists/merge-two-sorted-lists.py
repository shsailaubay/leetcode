# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        res = None
        curr = None
        while l1 or l2:
            mn = min([l1, l2], key=lambda x: getattr(x, 'val', 101))
            if not res:
                res = ListNode(mn.val)
                curr = res
            else:
                curr.next = ListNode(mn.val)
                curr = curr.next
            if l1 is mn:
                l1 = getattr(l1, 'next', None)
            else:
                l2 = getattr(l2, 'next', None)
        return res
            
            
            