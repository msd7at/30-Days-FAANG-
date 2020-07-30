# link ;  https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        ar=[1]*n
        m=1
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i] and ar[j]>=ar[i]:
                    ar[i]=ar[j]+1
                    m=max(m,ar[i])         
        return m
            
        
