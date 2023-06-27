import bisect

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        bf = False
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                e = [nums1[i], nums2[j]]
                bisect.insort_left(res, e, key=lambda x: sum(x))
                if i == 0 and len(res) == k:
                    break
                if len(res) > k:
                    l = res.pop()
                    if l == e:
                        break
 
        return res
            
            