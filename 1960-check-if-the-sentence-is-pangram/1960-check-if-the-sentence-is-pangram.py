class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        d={}
        c=0
        for i in sentence:
            if i not in d:
                c+=1
                d[i]=1
        if c==26:
            return True
        else:
            return False