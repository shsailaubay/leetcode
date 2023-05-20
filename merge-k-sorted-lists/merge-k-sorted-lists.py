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
            m = 0
            for i in range(0, len(lst)):
                if lst[i].val < lst[m].val:
                    m = i
            return m

        while lists:
            idx = min_index(lists)
            curr.next = lists[idx]
            curr = curr.next
            if lists[idx].next:
                lists[idx] = lists[idx].next
            else:
                lists.pop(idx)

        return r.next
