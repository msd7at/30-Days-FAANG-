link:-https://leetcode.com/problems/sort-colors/
TC:-O(n)   
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        h=len(nums)-1
        l,m=0,0
        while m<=h:
            if nums[m]==0:
                nums[m],nums[l]=nums[l],nums[m]
                l+=1
                m+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[h],nums[m]=nums[m],nums[h]
                h=h-1
