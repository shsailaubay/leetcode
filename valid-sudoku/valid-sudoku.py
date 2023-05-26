class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            v = set()
            h = set()
            for j in range(0, 9):
                vi = board[i][j]
                hi = board[j][i]
                if vi != ".":
                    if vi in v:
                        return False
                    v.add(vi)
                if hi != ".":
                    if hi in h:
                        return False
                    h.add(hi)
        for v in range(0, 3):
            for h in range(0, 3):
                s = set()
                for i in range(h * 3, h * 3 + 3):
                    for j in range(v * 3, v * 3 + 3):
                        val = board[i][j]
                        if val != ".":
                            if val in s:
                                return False
                            s.add(val)
        return True