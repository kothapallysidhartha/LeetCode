class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = ''

        sign = 1
        for i in str(x):
            if i == '-':
                sign = -1
            else:
                y += i
        y = sign * int(y[::-1])
        if y < -(2 ** 31) or y >(2**31 - 1):
            return 0
        return y
        
"""import sys

class Solution(object):
    def reverse(self, x):
        
        :type x: int
        :rtype: int
    
        o = 0
        n = 0
        
        if x < 0:
            n = 1
            x = -x
        
        while x != 0:
            # Check for overflow before updating o
            if o > sys.maxsize // 10 or (o == sys.maxsize // 10 and x % 10 > sys.maxsize % 10):
                return 0  # Return 0 for overflow cases
            
            o = (o * 10) + (x % 10)
            x = x // 10
        
        if n == 1:
            return -o
        else:
            return o
"""