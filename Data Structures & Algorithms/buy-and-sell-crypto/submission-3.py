class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        currentMin = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - currentMin > maxProf:
                maxProf = prices[i] - currentMin
            if prices[i] < currentMin:
                currentMin = prices[i]
        return maxProf