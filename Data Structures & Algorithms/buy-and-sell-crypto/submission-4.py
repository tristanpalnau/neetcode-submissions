class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        currentMin = prices[0]
        for i in range(1, len(prices)):
            maxProf = max(maxProf, prices[i] - currentMin)
            currentMin = min(currentMin, prices[i])
        return maxProf