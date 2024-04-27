class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        trimmed_string = s.strip()
        words = trimmed_string.split()
        if len(words) == 0:
            return 0
        return len(words[-1])