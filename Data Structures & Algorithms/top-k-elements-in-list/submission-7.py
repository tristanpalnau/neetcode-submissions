class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        for num in nums:
            count[num] += 1
        for key, val in count.items():
            freq[val].append(key)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                if len(res) < k:
                    res.append(num)
        return res