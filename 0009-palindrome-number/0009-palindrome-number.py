class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        st = str(x)
        j = -1
        flag = 0
        for i in range(len(st)//2):
            if st[i] != st[j]:
                flag = 1
                break
            j = j - 1
        if flag == 1:
            return False
        else:
            return True
