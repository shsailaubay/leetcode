# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        l = [root]
        t = None
        res = None
        j = 1
        while l:
            t = []
            s = 0
            for i in l:
                s += i.val
                if i.left:
                    t.append(i.left)
                if i.right:
                    t.append(i.right)
            l = t
            if res == None:
                res = (j, s)
            else:
                if res[1] < s:
                    res = (j, s)
            j += 1
        return res[0]