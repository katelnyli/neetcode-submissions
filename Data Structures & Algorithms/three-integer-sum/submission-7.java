class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int j = i + 1;
            int k = nums.length - 1;

            int target = -nums[i];

            while (j < k) {
                int sum = nums[j] + nums[k];
                if (target == sum) {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    k--;
                    j++;
                    while (nums[j] == nums[j - 1] && j < k) j++;
                    while (nums[k] == nums[k + 1] && j < k) k--;
                } else if (target < sum) {
                    k--;
                } else {
                    j++;
                }
            }
        }

        return res;
    }
}
