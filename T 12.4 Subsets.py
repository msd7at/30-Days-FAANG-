#link : https://leetcode.com/problems/subsets/
# explanation : https://leetcode.com/problems/subsets/discuss/723356/Python-3-Bit-Manipulation
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        l=len(nums)
        p=2**(l)
        for i in range(p):
            k=[]
            for j in range(l):
                if i & (1<<j)>0:
                    k.append(nums[j])
            ans.append(k)
        return ans
