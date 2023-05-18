class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
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
        result = ['',]
        for d_ in digits:
            d = chars[d_]
            result = [r+x for r in result for x in d]
        return result

