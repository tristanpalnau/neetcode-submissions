class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        left = [prices[0]]
        for i in range(1, len(prices)):
            if prices[i] - min(left) > maxProf:
                maxProf = prices[i] - min(left)
            left.append(prices[i])
        return maxProf
        