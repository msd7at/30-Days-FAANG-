class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        l=len(height)
        j=l-1
        ans=0
        maxleft=-1
        maxright=-1
        while i <j:
            if height[i] <= height[j]:
                maxleft=max(maxleft,height[i])
                ans= ans+maxleft- height[i]
                i+=1
            else:
                maxright=max(maxright,height[j])
                ans= ans +maxright-height[j]
                j-=1
        return ans
    
