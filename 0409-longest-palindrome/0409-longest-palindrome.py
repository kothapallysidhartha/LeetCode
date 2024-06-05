class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        length = 0
        odd_count_found = False
        
        for char in s:
            d[char] = d.get(char, 0) + 1
        
        for count in d.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_count_found = True
        
        if odd_count_found:
            length += 1
        
        return length
