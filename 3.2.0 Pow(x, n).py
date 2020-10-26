# link : https://leetcode.com/problems/powx-n/
#time complexity : logn
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def www(x,n):
            if n==0:
                return 1
            temp=self.myPow(x,n//2)
            if n%2==0:
                return temp*temp
            else:
                return temp*temp*x
        if n>=0:
            return www(x,n)
        else:
            return 1/www(x,-n)
