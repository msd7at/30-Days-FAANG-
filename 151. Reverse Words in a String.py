class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        temp=""
        st=0 
        e=len(s)-1
        # starting index (excluding space)
        for i in range(len(s)):
            if s[i]!=" ":
                st=i
                break
                
        # ending index (excluding space)
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                e=i
                break
        s=s[st:e+1]
        
        
        for i in s[::-1]:
            if i==" ":
                if temp!="":
                    ans+=temp+i
                    temp=""
            else:
                temp=i+temp
        ans+=temp
        return(ans)
            
                
                
                
