class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        news = ""
        chars = "abcdefgghijklmnopqrstuvwxyz0123456789"
        
        for i in range(len(s)):
            if s[i] in chars:
                news += s[i]
            
        s = news
        
        i, j = 0, len(s) - 1
        
        while i < len(s):
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True