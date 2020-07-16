#link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# explanation :https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/739578/Python-3-greedy(activity-selection)-beats-80-solutions
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x:x[1])
        l=len(points)
        if l==0:
            return l
        c=1
        prev=points[0][1]
        for i in range(1,l):
            if points[i][0]>prev:
                c+=1
                prev=points[i][1]
        return c
