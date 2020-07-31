# link:  https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[]
        for i in range(n+1):
            pp=[]
            for j in range(m+1):
                pp.append(0)
            dp.append(pp)
        for i in range(1,n+1):
            a=text1[i-1]
            for j in range(1,m+1):
                b=text2[j-1]
                if a==b:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
            
        
        
