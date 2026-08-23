class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        best = 0
        for i in range(n):
            if prices[i] < buy:
                buy = prices[i]
            else:
                best = max(best,prices[i] - buy)
        return best