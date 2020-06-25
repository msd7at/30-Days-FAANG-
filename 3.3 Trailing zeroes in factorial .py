#  https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans=0
        i=5
        while n//i>0:
            ans+= (n//i)
            i*=5
        return ans
