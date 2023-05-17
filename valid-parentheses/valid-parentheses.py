class Solution:
    def isValid(self, s: str) -> bool:
        c = 0
        while c < 3 and s:
            n = s.replace('()', '').replace('{}', '').replace('[]', '')
            c += n == s
            s = n
        return len(s) == 0

