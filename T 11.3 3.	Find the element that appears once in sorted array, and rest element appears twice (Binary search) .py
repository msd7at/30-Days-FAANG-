# link :  https://leetcode.com/problems/single-element-in-a-sorted-array/
# explan  :https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/742785/Python-binary-search-simple-solution
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        if high==0:
            return nums[0]
        elif nums[0]!=nums[1]:
            return nums[0]
        elif nums[high]!=nums[high-1]:
            return nums[high]
        while low<=high:
            mid=low+((high-low)//2)
            if nums[mid+1]!=nums[mid] and nums[mid-1]!=nums[mid]:
                return nums[mid]
            elif mid%2==0 and nums[mid+1]==nums[mid] or mid%2==1 and nums[mid-1]==nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1
            
            
            
