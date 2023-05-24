import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums2, nums1), key = lambda z: z[0], reverse = True)
        heap = []

        res = 0
        total = 0

        for i in range(0, len(nums)):
            heapq.heappush(heap, nums[i][1])
            total += nums[i][1]
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                res = max(res, total * nums[i][0])
        return res

