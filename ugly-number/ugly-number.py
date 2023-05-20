class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        _n = False
        while True:
            if n == 1:
                return True
            _n = False
            for i in [5,3,2]:
                a, b = divmod(n, i)
                if b == 0:
                    n = a
                    _n = True
                    break
            if not _n:
                break
        return False