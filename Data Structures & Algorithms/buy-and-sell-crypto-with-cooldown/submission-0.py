class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # top-down, key = (i, buying) val = max_profit
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cd = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cd)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cd)

            return dp[(i, buying)]
            
        return dfs(0, True)
