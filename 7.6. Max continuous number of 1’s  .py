# link https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s=0
        m=0
        for i in nums:
            if i==0:
                s=0
            else:
                s=s+1
                m=max(s,m)
        return m
