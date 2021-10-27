# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            temp=l1
            l1=l2
            l2=temp
        res=l1
        while l1 and l2:
            temp=None
            while l1 and l1.val<=l2.val:
                temp=l1
                l1=l1.next
            temp.next=l2
        
            temp=l1
            l1=l2
            l2=temp 
        return res
