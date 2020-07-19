# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#link:https://leetcode.com/problems/intersection-of-two-linked-lists/
class Solution:
    def getIntersectionNode(self, heada: ListNode, headb: ListNode) -> ListNode:
        if not heada or not headb:
            return None
        a=heada
        b=headb
        while a!=b:
            if a!=None:
                a=a.next
            else:
                a=headb
            if b!=None:
                b=b.next
            else:
                b=heada
        return a
            
