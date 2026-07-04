class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {
                int target = -nums[i];
                int sum = nums[j] + nums[k];

                if (sum == target) {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;
                    k--;
                    while (nums[j] == nums[j - 1] && j < k) j++;
                    while (nums[k] == nums[k + 1] && j < k) k--;
                } else if (sum < target) {
                    j++;
                } else {
                    k--;
                }
            }
        }

        return res;
    }
}
