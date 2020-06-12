#kadanes Algo
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        meh=0
        msf=min(nums)
        for i in nums:
            meh=meh+i
            if meh<i:
                meh=i
            if msf < meh:
                msf=meh
        return msf 
                    
