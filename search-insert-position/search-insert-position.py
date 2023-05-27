class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        e = list(enumerate(nums))
        def search(lst) -> int:
            
            center = len(lst) // 2
            if lst[center][1] == target:
                return lst[center][0]
            elif lst[center][1] < target:
                if center == len(lst) - 1:
                    return lst[center][0] + 1
                return search(lst[center:])
            else:
                if center == 0:
                    return lst[center][0]
                return search(lst[:center])
        return search(e)