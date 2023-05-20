class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        t = set()
        if target >= 3000:
            return nums[-1] + nums[-2] + nums[-3]
        elif target <= -3000:
            return nums[0] + nums[1] + nums[2]

        def diff(a, b):
            return abs(a - b)
        
        def bins(s: int, lst: List[int]) -> int:
            if len(lst) == 1:
                return lst[0]
            center = len(lst) // 2
            el = lst[center]
            d = target - s + el
            if d == 0:
                return lst[center]
            if s + lst[center] > target:
                lst = lst[0: center]
            else:
                lst = lst[center: len(lst)]
            if len(lst) == 0:
                return el
            return bins(s, lst)

        closest = None
        _c_diff = None
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                if s in t:
                    continue
                t.add(s)
                lst = nums[i + 1:j] + nums[j+1:len(nums)]
                if len(lst) == 0:
                    continue
                _new_cl = bins(s, lst)
                _new_diff = diff(target, s + _new_cl)

                if closest == None:
                    closest = s + _new_cl
                    _c_diff = _new_diff
                if _new_diff == 0:
                    return s + _new_cl
                if _new_diff < _c_diff:
                    closest = s + _new_cl
                    _c_diff = _new_diff
    
        return closest
                