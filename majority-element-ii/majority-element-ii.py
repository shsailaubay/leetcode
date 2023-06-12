from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = int(len(nums) / 3)
        count = Counter(nums)
        return [e for e, c in count.items() if c > t]