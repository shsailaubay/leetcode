from functools import cache

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = set([(c, ) for c in candidates if c == target])
        candidates = [c for c in candidates if c < target]

        @cache
        def make(n: int) -> Set[int]:
            pull = set()
            for c in candidates:
                if c == n:
                    pull.add((c,))
                elif n > c:
                    pull_ = make(n - c)
                    for e  in pull_:
                        pull.add(tuple(sorted((c,) + e)))
            return pull

        for i in candidates:
            res.update(make(target))

        return list(map(list, res))


