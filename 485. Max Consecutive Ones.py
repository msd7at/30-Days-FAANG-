class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s=0
        m=0
        for i in nums:
            if i ==0:
                s=0
            else:
                s+=1
            m=max(m,s)
        return m
