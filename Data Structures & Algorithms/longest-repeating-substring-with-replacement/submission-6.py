from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_count = 0
        res = 0
        counts= defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1
            max_count = max(max_count, counts[s[r]])
            if (r-l+1) - max_count <= k:
                res = max(res, (r-l+1))
            else:
                counts[s[l]] -= 1
                l += 1
        return res