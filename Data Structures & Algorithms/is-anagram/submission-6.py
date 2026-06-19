class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = collections.Counter(s)
        for c in t:
            if count[c] <= 0:
                return False
            count[c] -= 1
        return True