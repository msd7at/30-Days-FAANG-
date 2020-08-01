# https://leetcode.com/problems/detect-capital/
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c=0
        for i in word:
            if i.isupper():
                c+=1
        if c==0:
            return True
        else:
            if c==1:
                if word[0].isupper():
                    return True
                return False
            if c==len(word):
                return True
        return False
