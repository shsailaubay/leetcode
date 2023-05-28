class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = -10001
        
        for n in nums:
            s += n
            m = max(s, m)

            if s < 0:
                s = 0
        
        return m
