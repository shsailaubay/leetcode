from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        t = Counter(list(zip(*grid)))
        grid = map(tuple, grid)
        c = 0
        for e in grid:
            c += t[e]
        return c