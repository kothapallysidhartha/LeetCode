class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        si= 1
        i = 0
        l = len(s)
        
        while i < l and s[i] == ' ':
            i += 1
        if i < l and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                si = -1
            i += 1
        while i < l and s[i].isdigit():
            n = n * 10 + int(s[i])
            i += 1
        n *= si
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if n > INT_MAX:
            return INT_MAX
        if n < INT_MIN:
            return INT_MIN
        
        return n
