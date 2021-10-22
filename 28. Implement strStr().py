class Solution:
    def strStr(self, txt: str, pat: str) -> int:
        if pat=="":
            return 0
        d=256
        q=101
        n,m=len(txt),len(pat)
        if n<m:
            return -1
        i,j,p,t,h=0,0,0,0,1
        for i in range(m-1):
            h=(h*d)%q
        for i in range(m):
            p = (d*p + ord(pat[i]))%q
            t = (d*t + ord(txt[i]))%q
        for i in range(n-m+1):
            if p==t:
                for j in range(m):
                    if txt[i+j] != pat[j]:
                        break
                    else: j+=1
                    if j==m:
                        return i
            if i < n-m:
                t = (d*(t-ord(txt[i])*h) + ord(txt[i+m]))%q
                if t < 0:
                    t = t+q
        return -1
