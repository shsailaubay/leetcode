class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        counter = dict()
        for i in nums:
            if i not in counter:
                 counter[i] = 0
            if (i * 4 == target and counter[i] < 4) or counter[i] < 3:
                counter[i] += 1
        nums = [[x] * v for x, v in counter.items()]
        nums = [x for row in nums for x in row]
        tuples = dict()
        tuples_vals = set()
        res = set()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if s not in tuples:
                    tuples[s] = []
                sv = tuple(sorted([i, j]))
                if sv in tuples_vals:
                    continue
                tuples_vals.add(sv)
                tuples[s].append(( i, j ))
        for key, values in tuples.items():
            candidate = target - key
            if candidate in tuples:
                variants = tuples[candidate]
                for i, j in values:
                    for v in variants:
                        if i in v or j in v:
                            continue
                        res.add(tuple(sorted([nums[i], nums[j], nums[v[0]], nums[v[1]]])))

        return map(list, res)
