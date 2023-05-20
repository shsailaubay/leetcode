class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = set()
        minset = {1,2,3}
        while len(s) < n:
            _m = min(minset)
            s.add(_m)
            minset.remove(_m)
            minset.update([_m * 2, _m * 3, _m * 5])
        return list(sorted(s))[n - 1]
        