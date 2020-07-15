# link    https://leetcode.com/problems/count-and-say/
# explain   https://leetcode.com/problems/count-and-say/discuss/736691/Python-3

class Solution:
    def countAndSay(self, n: int) -> str:
        ar=[]
        def help(s):
            result=[]
            i=0
            while i< len(s):
                c=1
                while i+1<len(s)and s[i]==s[i+1]:
                    i+=1
                    c+=1
                result.append(str(c)+s[i])
                i+=1
            return ''.join(result)
        s="1"
        for i in range(n-1):
            s=help(s)
        return s
        
        
