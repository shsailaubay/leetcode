class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(lst: List[int], startIndex: int) -> int:
            if len(lst) == 0:
                return -1
            center = len(lst) // 2
            if lst[center] == target:
                return startIndex + center
            elif lst[center] > target:
                return search(lst[:center], startIndex)
            return search(lst[center + 1:], center + startIndex + 1)
        
        index = search(nums, 0)

        if index == -1:
            return [-1, -1]
        
        i = j = index

        i_c = j_c = False

        while i_c == False or j_c == False:

            if i - 1 >= 0:
                p = nums[i - 1]
                if p == target:
                    i -= 1
                else:
                    i_c = True
            else:
                i_c = True

            if j + 1 < len(nums):            
                n = nums[j + 1]

                if n == target:
                    j += 1
                else:
                    j_c = True
            else:
                j_c = True
        
        return [i, j]
