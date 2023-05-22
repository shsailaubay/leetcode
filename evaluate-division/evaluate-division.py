from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(dict)
        visited = set()

        def add(a, b, val):
            if (a, b) not in visited:
                visited.add((a, b))
                d[a][b] = val

                for i in list(d.keys()):
                    if a in d[i]:
                        d[i][b] = d[i][a] * val
                
                if b in d:
                    for k, v in list(d[b].items()):
                        add(a, k, v * val) 

        for i in range(0, len(equations)):
            a, b = equations[i]
            val = values[i]

            add(a, b, val)
            add(b, a, 1 / val)

        res = []
        for a, b in queries:
            if a not in d:
                res.append(-1)
                continue
            res.append(d[a].get(b, -1))

        return res
            

                        
