#link:        https://leetcode.com/problems/longest-common-prefix/
#explanation: https://leetcode.com/problems/longest-common-prefix/discuss/734809/Python-3-32ms-Simple-solution-without-using-zip
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m=1000000000000
        for i in strs:
            m=min(m,len(i))
        if m==0 or strs==[]:
            return ""
        ans=""
        for i in range(m):
            x=1 
            for j in range(len(strs)):
                if j==0:
                    te=strs[j][i]

                else:
                    
                    if te!=strs[j][i]:
                        x=11
                        break
        
            if x==1:
                ans=ans+te
            else:
                break
        return ans
                    
