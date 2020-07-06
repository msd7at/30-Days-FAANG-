# link : https://leetcode.com/problems/power-of-two/
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        if n<=0:
            return False
        return 2**int(math.log(n,2))==n"""
        if n >0:
            if n & n-1==0:
                return True
        return False
