class Solution:

    def longestPalindrome(self, s: str) -> str:
        max_p = ""

        def check_palindrome(i, j) -> str:
            while True:
                if i == 0 or j == len(s) - 1:
                    return s[i:j + 1]
                i -= 1
                j += 1
                if s[i] != s[j]:
                    return s[i + 1:j]
            
        
        for ind in range(0, len(s) - 1):
            p = check_palindrome(ind, ind)
            if len(p) > len(max_p):
                max_p = p
            if s[ind] == s[ind + 1]:
                p = check_palindrome(ind, ind + 1)
                if len(p) > len(max_p):
                    max_p = p
        
        if s[len(s) - 2] == s[len(s) - 1]:
                p = check_palindrome(len(s) - 2, len(s) - 1)
                if len(p) > len(max_p):
                    max_p = p

        return max_p