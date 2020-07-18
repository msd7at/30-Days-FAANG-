# link : https://leetcode.com/problems/search-in-rotated-sorted-array/
# explanation    https://www.youtube.com/watch?v=oTfPJKGEHcc
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        n=len(nums)
        h=n-1
        while l<=h:
            mid=((l+h)//2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[l] :
                if target <= nums[mid] and target>=nums[l]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if target>=nums[mid] and target <=nums[h]:
                    l=mid+1
                else:
                    h=mid-1
        return -1
        
