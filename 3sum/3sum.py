class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) > 3:
            nums = sorted(nums)
            d = dict()
            for pos, el in enumerate(nums):
                if el not in d:
                    d[el] = [pos]
                else:
                    d[el].append(pos)
            three = set()
            for i in range(0, len(nums)):
                for j in range(i+1, len(nums)):
                    tmp = 0 - (nums[i] + nums[j])
                    if tmp in d:
                        inds = d[tmp]
                        if len(inds) > 2 or (inds != [i, j] and inds != [j, i] and inds != [i] and inds != [j]):
                            three.add(tuple(sorted([nums[i], nums[j], tmp])))
                        
            return map(list, three)

        elif len(nums) == 3 and sum(nums) == 0:
            return [nums]
        return []