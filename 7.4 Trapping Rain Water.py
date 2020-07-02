# link : https://leetcode.com/problems/trapping-rain-water/
# explanation  https://leetcode.com/problems/trapping-rain-water/discuss/715404/Python-3-Two-pointers-48-ms-Soln

class Solution:
    def trap(self, nums: List[int]) -> int:
        h=len(nums)-1
        l=0
        rs=0
        lf=0
        rt=0
        while l<=h:
            if nums[l]< nums[h]:
                if lf < nums[l]:
                    lf= nums[l]
                else:
                    rs= rs + lf - nums[l]
                l+=1
            else:
                if rt < nums[h]:
                    rt=nums[h]
                else:
                    rs= rs + rt -nums[h]
                h-=1
        return rs
