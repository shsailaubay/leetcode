from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = []
        pull: List[Set[str]] = list()
        for e in s:
            new_pull: List[Set[str]] = []
            for p in pull:
                if e in p:
                    if len(m) < len(p):
                        m = p
                else:
                    p.add(e)
                    new_pull.append(p)
            new_pull.append({e})
            pull = new_pull
        pull.append(m)
        return max(map(len, pull))
