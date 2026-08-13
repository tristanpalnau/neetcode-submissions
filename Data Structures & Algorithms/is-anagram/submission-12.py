class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = [0] * 26
        count_t = [0] * 26
        for i in range(len(s)):
            s_pos = ord(s[i]) - ord('a')
            t_pos = ord(t[i]) - ord('a')
            count_s[s_pos] += 1
            count_t[t_pos] += 1
        return count_s == count_t