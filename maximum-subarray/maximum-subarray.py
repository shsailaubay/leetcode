class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = -10001
        i = 0
        s_res = True

        while i < len(nums):
            if s + nums[i] <= 0:
                if s_res:
                    m = max(m, nums[i])
                else:
                    m = max(m, s)
                s = 0
                s_res = True
            else:
                if nums[i] < 0 and not s_res:
                    m = max(m, s)
                s += nums[i]
                s_res = False
            
            i += 1
        if not s_res:
            m = max(m, s)
        
        return m
