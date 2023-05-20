# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        r = ListNode()
        curr = r

        lists = [e for e in lists if e]
        if not len(lists):
            return r.next

        def min_index(lst: List[Optional[ListNode]]) -> int:
            return 

        while lists:
            idx = lists.index(min(lists, key=lambda x: getattr(x, 'val')))
            curr.next = lists[idx]
            curr = curr.next
            if lists[idx].next:
                lists[idx] = lists[idx].next
            else:
                lists.pop(idx)

        return r.next
