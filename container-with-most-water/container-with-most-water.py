class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        i = 0
        j = len(height) - 1
        height_max = max(height)
        while i < j:
            mx = max(mx, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            if height_max * (j - i) <= mx:
                break
        return mx
        