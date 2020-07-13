# link :https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        add=0
        i=0
        while i<len(s):
            if(i==len(s)-1):
                add+=d[s[i]]
                break
            if(d[s[i]]<d[s[i+1]]):
                add=add+(d[s[i+1]]-d[s[i]])
                i+=1
            else:
                add=add+d[s[i]]
            i+=1
        return add
        
