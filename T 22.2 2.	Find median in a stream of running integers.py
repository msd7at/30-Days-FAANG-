# link: https://leetcode.com/problems/find-median-from-data-stream/
import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.c=0
        self.q=[]

    def addNum(self, num: int) -> None:
        bisect.insort(self.q, num)
        self.c+=1

    def findMedian(self) -> float:
        if self.c%2==1:
            return self.q[self.c//2]
        else:
            return (self.q[self.c//2]+self.q[(self.c//2)-1])/2
