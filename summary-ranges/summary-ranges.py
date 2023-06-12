class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        tmp = [[nums[0], nums[0]]]

        for i in range(1, len(nums)):
            if nums[i] - tmp[-1][1] == 1:
                tmp[-1][1] = nums[i]
                continue
            tmp.append([nums[i], nums[i]])

            
        return map(lambda x: "{}->{}".format(*x) if x[0] != x[1] else str(x[0]), tmp)
            
