class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // count frequencies w hashmap
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // create and fill buckets to collect top k. each index represents the freq.
        List<Integer>[] buckets = new List[nums.length + 1];
        
        for (int num : map.keySet()) {
            int freq = map.get(num);
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(num);
        }

        int[] res = new int[k];
        int c = 0;
        for (int i = buckets.length - 1; i >= 0 && c < k; i--) {
            if (buckets[i] != null) {
                for (int num : buckets[i]) {
                    res[c] = num;
                    c++;
                    if (c == k) return res;
                }
            }
        } 
        return res;
    }
}
