class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        el = list(map(int, num))
        m = False
        for i in range(0, len(el)):
            e = el[i]
            j = change[e]
            if j < e and m:
                break
            if j > e:
                el[i] = j
                m = True
        return "".join(map(str, el))

