# link   https://leetcode.com/problems/longest-palindromic-substring/
# explanation  https://leetcode.com/problems/longest-palindromic-substring/discuss/733237/Python-3-2-Methods
class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        m=1
        st=0
        low=0
        high=0
        for i in range(1,n):
            # for even pallindrome
            low=i-1
            high=i
            while low >=0 and high <n and s[low]==s[high]:
                if high-low+1 > m:
                    st=low
                    m=high-low+1
                low-=1
                high+=1
            # for odd pallindrome
            low=i-1
            high=i+1
            while low >=0 and high <n and s[low]==s[high]:
                if high-low+1 > m:
                    st=low
                    m=high-low+1
                low-=1
                high+=1
        return s[st:st+m]   
    """
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[]
        for i in range(n):
            temp=[0]*n
            temp[i]=1
            dp.append(temp)
        m=1
        st=0
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=1
                st=i
                m=2
        k=3
        for k in range(k,n+1):
            for i in range(n-k+1):
                j=i+k-1
                if s[i]==s[j] and dp[i+1][j-1]==1:
                    dp[i][j]=1
                    if m<k:
                        m=k
                        st=i
                    
        return s[st:st+m]
"""
        
