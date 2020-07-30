#link:  https://leetcode.com/problems/maximum-product-subarray/
# method 1
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        cur=1
        for i in nums:
            cur=i*cur
            ans=max(ans,cur)
            if cur==0:
                cur=1
        cur=1
        for i in range(len(nums)-1,-1,-1):
            cur=nums[i]*cur
            ans=max(ans,cur)
            if cur==0:
                cur=1
        return ans
 # method 2
 class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pma=nums[0]
        pmi=nums[0]
        cmi=nums[0]
        cma=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            cma=max(max(pma*nums[i],pmi*nums[i]),nums[i])
            cmi=min(min(pma*nums[i],pmi*nums[i]),nums[i])
            pma=cma
            pmi=cmi
            ans=max(cma,ans)
        return ans
