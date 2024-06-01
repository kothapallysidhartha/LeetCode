import java.util.Stack;
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        String openingBrackets = "([{";
        String closingBrackets = ")]}";
        
        Map<Character, Character> bracketPairs = new HashMap<>();
        bracketPairs.put(')', '(');
        bracketPairs.put(']', '[');
        bracketPairs.put('}', '{');
        
        for (char c : s.toCharArray()) {
            if (openingBrackets.indexOf(c) != -1) {
                stack.push(c);
            } else if (closingBrackets.indexOf(c) != -1) {
                if (stack.isEmpty() || stack.peek() != bracketPairs.get(c)) {
                    return false;
                }
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String input = "()[]{}";  // example input
        boolean output = solution.isValid(input);
        System.out.println("Input: " + input);
        System.out.println("Output: " + output);
    }
}
