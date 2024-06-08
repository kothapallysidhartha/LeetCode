class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        m = 0
    
        for i in nums:
            if i % 2 == 0:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
    
        mosteven = None
        maxx = 0
        for key, value in d.items():
            if value > maxx:
                mosteven = key
                maxx= value
            elif value == maxx:
                mosteven = min(mosteven, key)
        #ternery condition [ stm1-->{exe} if {condition}-->{true} else stm 2-->{exe}]
        return mosteven if mosteven is not None else -1
