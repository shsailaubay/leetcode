class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_sum = len(nums1) + len(nums2)
        to = (len_sum // 2) + 1
        # if len_sum % 2 == 0:
        #     to -= 1
        m1, m2 = None, None
        i, j = len(nums1) - 1, len(nums2) - 1
        for _ in range(0, to):
            if i > -1 and j > -1:
                if nums1[i] > nums2[j]:
                    m1, m2 = m2, nums1[i]
                    i -= 1 
                else:
                    m1, m2 = m2, nums2[j] 
                    j -= 1
            elif i > -1:
                m1, m2 = m2, nums1[i]
                i -= 1 
            else:
                m1, m2 = m2, nums2[j] 
                j -= 1
        return (m1 + m2) / 2 if len_sum % 2 == 0 else m2

        