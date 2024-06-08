class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            x = ''.join(sorted(word))
            if x not in d:
                d[x] = [word]
            else:
                d[x] += [word]
        return list(d.values())