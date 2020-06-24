#link: https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, n: int) -> str:
        s=""
        for i in range(65,91):
            s=s+chr(i)
        st=""
        while n:
            n=n-1
            st=s[n%26]+st
            n=n//26
        return st
