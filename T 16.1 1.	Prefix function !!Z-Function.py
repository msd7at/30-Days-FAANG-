#https://leetcode.com/problems/implement-strstr/
# explain   https://leetcode.com/problems/implement-strstr/discuss/736574/Python-3-using-Z-Algorithm

class Solution:
    def strStr(self, text: str, pat: str) -> int:
        if pat=="":
            return 0
        
        con=pat+"$"+text
        left=0
        right=0
        k=0
        n=len(con)
        z=[0]*n
        for i in range(1,n):
            if right<i:
                left,right=i,i
                while right<n and con[right-left]==con[right]:
                    right+=1
                z[i]=right-left
                right-=1
            else:
                k=i-left
                if z[k]<right-i+1:
                    z[i]=z[k]
                else:
                    left=i
                    while right<n and con[right-left]==con[right]:
                        right+=1
                    z[i]=right-left
                    right-=1 
        for i in range(n):
            if z[i]==len(pat):
                return i-len(pat)-1
        return -1
                
        
