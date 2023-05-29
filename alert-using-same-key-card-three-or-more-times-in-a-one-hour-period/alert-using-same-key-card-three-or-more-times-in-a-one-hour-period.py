from collections import defaultdict
from bisect import insort

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def to_int(t) -> int:
            h, m = t.split(":")
            return (int(h) * 60) + int(m)

        names = defaultdict(list)

        for i in range(0, len(keyName)):
            names[keyName[i]].append(to_int(keyTime[i]))
        
        res = []

        for k, val in names.items():
            
            if len(val) < 3:
                continue
            val.sort()
            for i in range(0, len(val) - 2):
                if 0 <= val[i + 2] - val[i] <= 60:
                    res.append(k)
                    break
        
        return sorted(res)







            