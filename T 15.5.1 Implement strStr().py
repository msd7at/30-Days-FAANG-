# link :-> https://leetcode.com/problems/implement-strstr/
class Solution:
    def strStr(self, h: str, n: str) -> int:
        l=len(h)
        ll=len(n)
        if ll>l:
            return -1
        for i in range(0,l-ll+1):
            if h[i:i+ll]==n:
                return i
        return -1
        
