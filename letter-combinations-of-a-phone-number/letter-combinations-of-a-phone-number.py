from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        return filter(bool, map(lambda s: "".join(s), product(*(chars[d] for d in digits))))

