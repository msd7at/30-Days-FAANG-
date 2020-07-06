# link :https://leetcode.com/problems/divide-two-integers/
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Brute force 
        """
        sign= (-1 if((dividend < 0) ^ (divisor < 0)) else 1)
        dividend=abs(dividend)
        divisor=abs(divisor)
        quot=0
        while dividend>=divisor:
            dividend-=divisor
            quot+=1
        return sign*quot
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        sign= (-1 if((dividend < 0) ^ (divisor < 0)) else 1)
        dividend=abs(dividend)
        divisor=abs(divisor)
        temp=0
        quot=0
        for i in range(31,-1,-1):
            if temp+(divisor<<i)<=dividend:
                temp+= (divisor<<i)
                quot= quot| (1<<i)
        return sign*quot
        
