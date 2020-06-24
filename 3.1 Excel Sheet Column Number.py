#link:-  https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, s: str) -> int:
        l=len(s)
        to=0
        for i in range(l):
            oo=ord(s[i])-64
            to=to+((oo)*(26**(l-i-1)))
        return to
