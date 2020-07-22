#link: https://leetcode.com/problems/word-break-ii/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        se=set(wordDict)
        re=[]
        if self.check(s,se):
            self.dfs(s,se,'',re)
        return re
    def dfs(self,s,se,path,re):
        if not s:
            re.append(path[:-1])
            return 
        else:
            for i in range(1,len(s)+1):
                if s[:i] in se:
                    self.dfs(s[i:],se,path+s[:i]+" ",re)
    def check(self,s,se):
        dp=[False for _ in range(len(s)+1)]
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in se:
                    dp[i]=True
        return dp[-1]
