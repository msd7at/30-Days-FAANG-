# link:  https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        se=set(wordDict)
        n=len(s)
        dp = [False for _ in range(n + 1)]
        dp[0]=True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j]==True and s[j:i] in se:
                    dp[i]=True
        return dp[-1]
                
        
