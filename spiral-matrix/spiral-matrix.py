class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            for i in range(0, len(matrix) - 1):
                res.append(matrix[i].pop())
            matrix = [m for m in matrix if m]
            if not matrix:
                break
            res += reversed(matrix.pop())
            for i in range(len(matrix) - 1, 0, -1):
                res.append(matrix[i].pop(0))
            matrix = [m for m in matrix if m]
        return res