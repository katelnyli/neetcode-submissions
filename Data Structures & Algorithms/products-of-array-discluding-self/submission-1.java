class Solution {
    public int[] productExceptSelf(int[] nums) {
        // use one array and a single var to keep track of running product
        int n = nums.length;
        int[] res = new int[n];

        res[0] = 1;
        for (int i = 1; i < n; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }

        // stores the product of everything to the right
        int postFix = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= postFix;
            postFix *= nums[i];
        }

        return res;
    }
}  
