class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        l=len(s)
        i=0
        while i<l and s[i]== " ":
            i+=1
        if i<l and s[i]!="+" and s[i]!="-" and ord(s[i])<48 and ord(s[i])>57:
            return 0
        if i>=l:
            return 0
        si=0
        if s[i]=="+":
            si=1
            i+=1
        elif s[i]=="-":
            si=-1
            i+=1
        # print(si,s[i],i)
        if i<l and si!=0 and (s[i]=="+" or s[i]=="-"):
            return 0
        if si==0:
            si=1
        ans=0
        m=1
        g=""
        while i<l and ord(s[i])>=48 and ord(s[i])<=57:
            g+=s[i]
            i+=1
        for i in g[::-1]:
            ans= ans+(m)*int(i)
            # print(ans)
            m*=10

        ans= ans*si
        if ans>(2**31) -1:
            return (2**31) - 1
        if ans < -2**31:
            return -2**31
        # for 
        return ans
