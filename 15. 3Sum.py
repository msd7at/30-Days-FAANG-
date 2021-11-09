class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ll=len(nums)
        ans=set()
        for i in range(ll-1):
            a=nums[i]
            l=i+1
            r=ll-1
            while l<r:
                s=a+nums[l]+nums[r]
                if s==0:
                    ans.add((a,nums[l],nums[r]))
                    l+=1
                    r-=1
                elif s<0:
                    l+=1
                else:
                    r-=1
        return list(ans)
