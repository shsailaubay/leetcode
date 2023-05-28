class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tg = len(nums) - 1
        @cache
        def jump(ind: int) -> bool:
            # if nums[ind] == 0:
            #     return False
            if nums[ind] + ind >= tg:
                return True
            return any(jump(i + 1) for i in range(ind, ind + nums[ind]))
        
        return jump(0)