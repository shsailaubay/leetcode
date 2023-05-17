from collections import deque

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_sum = len(nums1) + len(nums2)
        to = (len_sum // 2) + 1
        center = None
        if len_sum % 2 == 0:
            to -= 1
        medians = deque(maxlen=2 if len_sum % 2 == 0 else 1)
        for i in range(len_sum - 1, to - 2, -1):
            if nums1 and nums2:
                if nums1[-1] > nums2[-1]:
                    medians.append(nums1.pop())
                else:
                    medians.append(nums2.pop())
            elif nums1:
                medians.append(nums1.pop())
            else:
                medians.append(nums2.pop())
        return sum(medians) / len(medians)

        
