class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = j = -1
        for n in range(0, len(nums)):
            if nums[n] == target:
                if i == -1:
                    i = n
                j = n

        return [i, j]