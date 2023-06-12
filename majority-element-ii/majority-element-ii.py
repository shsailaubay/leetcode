from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = int(len(nums) / 3)
        d = defaultdict(lambda: 0)
        res = set()

        for n in nums:
            d[n] += 1
            if d[n] > t:
                res.add(n)
        
        return res