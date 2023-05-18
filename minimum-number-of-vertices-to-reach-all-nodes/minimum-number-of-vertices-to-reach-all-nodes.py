class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        fp = {x for x, _ in edges}
        sp = {x for _, x in edges}
        return fp - sp