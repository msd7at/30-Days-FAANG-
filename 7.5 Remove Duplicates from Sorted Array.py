# link :- https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# explanation  https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/715314/Python-3-Simple-Solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        s=0
        for i in range(l):
            if nums[i]!=nums[s]:
                s+=1
                nums[s]=nums[i]
        return s+1    
