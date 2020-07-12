# https://leetcode.com/problems/reverse-string/discuss/731342/python-3-beats-9980-simple-solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=len(s)
        for i in range(1,l//2 +1):
            s[i-1],s[-i]=s[-i],s[i-1]
        return s
