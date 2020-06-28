link: https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        l=len(nums)
        for i in range(l):
            if nums[i] not in d:
                d[nums[i]]=[i]
            else:
                d[nums[i]].append(i)
        for i in d:
            if target-i in d :
                if i==target-i and len(d[i])>1:
                    return [d[i][0],d[i][1]]
                elif i==target-i and len(d[i])==1:
                    pass
                else:
                    return [d[i][0],d[target-i][0]]
