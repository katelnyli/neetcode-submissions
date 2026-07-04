class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();

        for (String s : strs) {
            int[] count = new int[26];
            // turn string into array of chars
            for (char c : s.toCharArray()) {
                // index that ascii val and increment by 1
                count[c - 'a']++;
            }

            // create unique key
            StringBuilder sb = new StringBuilder();
            for (int i : count) {
                sb.append('#'); // delimiter to separate counts
                sb.append(i);
            }
            String key = sb.toString();

            result.putIfAbsent(key, new ArrayList<>());
            // populate the corresponding arraylist
            result.get(key).add(s);
        }
        return new ArrayList<>(result.values());
    }
}
