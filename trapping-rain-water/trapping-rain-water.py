from collections import Counter

class Solution:
    def trap(self, height: List[int]) -> int:
        counts = Counter(height)
        counts[0] = 0
        i, res = 0, 0
        while i < len(height):
            counts[height[i]] -= 1
            counts += Counter()
            if len(counts) == 0:
                break

            tmp = 0
            h = min(height[i], max(counts.keys()))
            i += 1
            while h > height[i]:
                tmp += h - height[i]
                counts[height[i]] -= 1
                i += 1
            res += tmp

        return res

