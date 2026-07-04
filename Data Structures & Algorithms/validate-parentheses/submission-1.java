class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap<>(3);

        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                if (map.containsKey(c)) {
                    if (!map.get(c).equals(stack.pop())) {
                        return false;
                    }
                }
            }
        }

        if (!stack.isEmpty()) return false;
        return true;
    }
}
