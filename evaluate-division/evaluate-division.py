from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(defaultdict)
        for i in range(0, len(equations)):
            a, b = equations[i]
            d[a][b] = values[i]
            for e, itm in d.items():
                if a in itm and b not in itm:
                    itm[b] = itm[a] * values[i]
                if b in itm and a not in itm:
                    itm[a] = itm[b] / values[i]

            d[b][a] = 1 / values[i]

        for a in d:
            keys = list(d[a].keys())
            for k in keys:
                v = d[a][k]
                for b, bval in d[k].items():
                    if b in d[a] or b == a:
                        continue
                    d[a][b] = bval * v

        res = []
        for a, b in queries:
            if a not in d:
                res.append(-1)
                continue
            if a == b:
                res.append(1)
                continue 
            res.append(d[a].get(b, -1))
        return res
            

                        

