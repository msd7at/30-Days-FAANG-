class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        se=set(wordDict)
        n=len(s)
        dp = [False for _ in range(n + 1)]
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if dp[i]==True and s[i:j] in se:
                    dp[j]=True
        return dp[-1]
                
        
