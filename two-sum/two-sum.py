class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            el = target - nums[i]
            ind = nums.index(el) if el in nums else -1
            if ind > -1 and ind != i:
                return [i, ind]
        return None
