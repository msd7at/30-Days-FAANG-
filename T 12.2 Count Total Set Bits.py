# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n:
            c=c+(n&1)
            n=n>>1
        return c
        """
        c=0
        while n:
            n=n &n-1
            c=c+1
        return c
        """
