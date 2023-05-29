from collections import defaultdict
from bisect import insort

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        @cache
        def to_int(t) -> int:
            h, m = t.split(":")
            return (int(h) * 60) + int(m)

        names = defaultdict(list)

        for i in range(0, len(keyName)):
            insort(names[keyName[i]], to_int(keyTime[i]))

        @cache
        def in_one_hour(a, b) -> bool:
            # if a > 1380 and b < 60:
            #     b += 1440
            
            return 0 <= b - a <= 60
        
        res = []

        for k, val in names.items():

            # if val[-1] > 1380:
            #     if val[0] < 60:
            #         val.append(val[0])
            #     if val[1] < 60:
            #         val.append(val[1])
            
            if len(val) < 3:
                continue
            
            for i in range(0, len(val) - 2):
                if in_one_hour(val[i], val[i + 2]):
                    res.append(k)
                    break
        
        return sorted(res)







            