from heapq import heapify, heappush, heappop

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = 1
        s = set()
        minset = [1,2,3]
        heapify(minset)
        while len(s) < n:
            _m = heappop(minset)
            if _m in s:
                continue
            s.add(_m)
            res = _m
            heappush(minset, _m * 2)
            heappush(minset, _m * 3)
            heappush(minset, _m * 5)
        return res
        