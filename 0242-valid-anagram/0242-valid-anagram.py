class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq1 = {}
        freq2 = {}
        
        for i in range(len(s)):
            if freq1.get(s[i]):
                freq1[s[i]] += 1
            else:
                freq1[s[i]] = 1
            
            if freq2.get(t[i]):
                freq2[t[i]] += 1
            else:
                freq2[t[i]] = 1
        
        for i in freq1:
            if not freq2.get(i) or freq1[i] != freq2[i]:
                return False
        
        return True