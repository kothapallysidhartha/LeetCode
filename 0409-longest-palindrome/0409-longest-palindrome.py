class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicty = {}
        for char in s:
            if char in dicty:
                dicty[char] += 1
            else:
                dicty[char] = 1
        
        max_len = 0
        max_odd = 0
        for val in dicty.values():
            if val % 2 == 0:
                max_len += val
            else:
                max_len += val - 1  
                max_odd = 1
        
        return max_len + max_odd