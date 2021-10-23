class Solution:
    def countAndSay(self, n: int) -> str:
        def ans(s):
            ans=""
            i=0
            while i < len(s):
                c=1
                while i+1 < len(s) and s[i]==s[i+1]:
                    c+=1
                    i+=1
                ans= ans+str(c)+s[i]
                i+=1
            return ans
        s="1"
        for i in range(n-1):
            s=ans(s)
        return s
