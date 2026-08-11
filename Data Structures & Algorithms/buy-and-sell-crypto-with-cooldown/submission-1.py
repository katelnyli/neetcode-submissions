class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = [float("-inf")] * n
        sell = [0] * n

        if n == 1:
            return 0

        for i in range(n):
            sell[i] = max(sell[i - 1], prices[i] + buy[i - 1])
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
        
        return sell[-1]

        