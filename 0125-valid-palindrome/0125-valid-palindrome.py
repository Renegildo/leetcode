class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        news = ""
        chars = [
            ",", ":", " ", ".", "@", "#", "_", "\\", "{", "}", "[", "]", "'", "\"", "-", "?",
            ";", "!", "(", ")", "`"
        ]
        
        for i in range(len(s)):
            if s[i] not in chars:
                news += s[i]
            
        print(news)
        s = news
        
        i, j = 0, len(s) - 1
        
        while i < len(s):
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True