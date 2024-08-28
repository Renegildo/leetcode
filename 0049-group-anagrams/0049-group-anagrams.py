class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = {}
        
        for s in strs:
            joined = ''.join(sorted(s))
            if joined in anagrams:
                anagrams[joined].append(s)
            else:
                anagrams[joined] = [s]
        
        j = 0
        for k in anagrams:
            res.append([])
            res[j] = anagrams[k]
            j += 1
        
        return list(res)