class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        for dec, roman in ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')):
            if dec > 1:
                while num >= dec:
                    remainder, num = divmod(num, dec)
                    if remainder > 0:
                        res += roman * remainder
            else:
                res += roman * num
        return res

