class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening_brackets = "([{"
        closing_brackets = ")]}"
        bracket_pairs = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if not stack or stack[-1] != bracket_pairs[char]:
                    return False
                stack.pop()
            else:
                # Invalid character
                return False
        return len(stack) == 0
