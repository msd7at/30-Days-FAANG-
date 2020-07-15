# link:       :https://leetcode.com/problems/implement-strstr/
# explanation :https://leetcode.com/problems/implement-strstr/discuss/738264/python-3-using-knuth-morris-pratt-algorithmkmp
class Solution:
    def strStr(self, text: str, pat: str) -> int:
        if text==pat:
            return 0
        if pat=="":
            return 0
        def patlps(pat,lps,m):
            left=0
            i=1
            while i<m:
                if pat[left]==pat[i]:
                    left+=1
                    lps[i]=left
                    i+=1
                else:
                    if left!=0:
                        left=lps[left-1]
                    else:
                        lps[i]=0
                        i+=1
        n=len(text)
        m=len(pat)
        lps=[0]*m
        patlps(pat,lps,m)
        j=0
        i=0
        while i<n:
            if pat[j]==text[i]:
                i+=1
                j+=1
            if j==m:
                return i-j
            elif i<n and pat[j]!=text[i]:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return -1
