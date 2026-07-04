class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        int[] dp = new int[prices.length];
        // dp[i] = min price from indexes 0..i
        dp[0] = prices[0];
        for (int i = 1; i < dp.length; ++i) {
            int profit = prices[i] - dp[i - 1];
            if (profit > maxP) maxP = profit;
            if (prices[i] < dp[i - 1]) {
                dp[i] = prices[i];
            } else {
                dp[i] = dp[i - 1];
            }
            
        }
        return maxP;
    }
}
