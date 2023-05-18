class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        fp = [x for x, _ in edges]
        sp = set([x for _, x in edges])
        return list(dict.fromkeys([x for x in fp if x not in sp]))