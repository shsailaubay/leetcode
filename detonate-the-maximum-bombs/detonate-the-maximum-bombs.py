from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def calc_gipotenuze(b1: List[int], b2: List[int]) -> int:

            a = abs(b1[0] - b2[0])
            b = abs(b1[1] - b2[1])

            if a == 0:
                return b
            
            if b == 0:
                return a

            return ((a ** 2) + (b ** 2)) ** (1/2)
        
        def is_intersect(i1: int, i2: int) -> bool:
            """
            :param i1: bomb a index
            :param i2: bomb b index
            """

            b1 = bombs[i1]
            b2 = bombs[i2]

            g = calc_gipotenuze(b1, b2)

            return g <= b1[2]
        
        intersects = defaultdict(set)

        for i in range(0, len(bombs)):
            intersects[i].add(i)
            for j in range(0, len(bombs)):
                if i == j:
                    continue
                if is_intersect(i, j):
                    intersects[i].add(j)
                    intersects[i].update(intersects[j])

                    for k, v in intersects.items():
                        if i in v:
                            v.add(j)

        for k, v in intersects.items():
            for i in list(v):
                v.update(intersects[i])


        if len(intersects.values()) == 0:
            return 1

        return max(map(len, intersects.values()))
                
