class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        st=0
        m=1
        low=0
        high=0
        for i in range(1,n):
            low=i-1
            high=i
            while low>=0 and high<n and s[low] == s[high]:
                if high-low+1 > m:
                    m=high-low+1
                    st=low
                low-=1
                high+=1
            low=i-1
            high=i+1
            while low>=0 and high<n and s[low] == s[high]:
                if high-low+1 > m:
                    m=high-low+1
                    st=low
                low-=1
                high+=1
        return s[st:st+m]
class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[]
        for i in range(n):
            tempDp=[0]*n
            tempDp[i]=1
            dp.append(tempDp)
        st=0
        m=1
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=1
                st=i
                m=2
        k=3
        while k <=n:
            i=0
            while i<n-k+1:
                j=i+k-1
                if s[i]== s[j] and dp[i+1][j-1]==1:
                    dp[i][j]=1
                    if k>m:
                        st=i
                        m=k
                i+=1
            k+=1
        return s[st:st+m]
            
            
