#link:- https://leetcode.com/problems/implement-strstr/
class Solution:
    def strStr(self, text: str, pat: str) -> int:
        if text==pat or pat=="":
            return 0
        d=26 # no of char in input alphabet
        M=len(pat)
        N=len(text)
        if M>N:
            return -1
        q=5381 # any prime no to avoid hash collision ,greater will be effective
        i,j=0,0
        p=0 # hash value for pattern
        t=0 # hash value for text
        h=1
        # The value of h would be "pow(d, M-1)%q" 
        for i in range(M-1): 
            h = (h*d)%q 
        for i in range(M):
            p=(d*p+ord(pat[i]))%q
            t=(d*t+ord(text[i]))%q
        for i in range(N-M+1):
            if p==t:
                for j in range(M):
                    if text[i+j]!=pat[j]:
                        break
                j+=1
                if j==M:
                    return i
            if i < N-M: 
                t = (d*(t-ord(text[i])*h) + ord(text[i+M]))%q 
                if t < 0: 
                    t = t+q 
        return -1
