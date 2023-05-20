class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in [5, 2, 3]:
            while n % i == 0:
                n //= i
        return n == 1