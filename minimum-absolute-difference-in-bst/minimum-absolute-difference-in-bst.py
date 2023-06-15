# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        m = []
        q = [root]
        t = None
        while q:
            t = []
            for e in q:
                m.append(abs(e.val))
                if e.left:
                    t.append(e.left)
                if e.right:
                    t.append(e.right)
            q = t
        m.sort()
        res = None
        for i in range(0, len(m) - 1):
            d = m[i+1] - m[i]
            if res == None:
                res = d
            res = min(res, d)
        return res