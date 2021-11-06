class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[s]:
                s+=1
                nums[s]=nums[i]
        return s+1
            
                
                
