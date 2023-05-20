from math import sqrt, ceil
from array import array

class Solution:

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = array('H', [1] * n)
        primes[0] = primes[1] = 0 

        for i in range(2, ceil(sqrt(n))):

            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = 0
        
        return sum(primes)

