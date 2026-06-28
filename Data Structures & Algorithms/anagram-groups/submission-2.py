class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        if not strs:
            return []
        for i in strs:
            word = [0] * 26
            for j in i:
                pos = ord(j) - ord('a')
                word[pos] = 1 + word[pos]
            words.setdefault(tuple(word), []).append(i)
        
        return list(words.values())

        
