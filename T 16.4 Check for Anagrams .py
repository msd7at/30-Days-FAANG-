# link: https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        dd={}
        for i in t:
            if i not in dd:
                dd[i]=1
            else:
                dd[i]+=1
        for i in d:
            if i not in dd :
                return False
            elif d[i]!=dd[i]:
                return False
        return True
