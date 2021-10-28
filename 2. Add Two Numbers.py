# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        x=res
        c=0
        s=0
        while l1 or l2 or c:
            if l1:
                c+=l1.val
                l1=l1.next
            if l2:
                c+=l2.val
                l2=l2.next
            res.next=ListNode(c%10)
            res=res.next
            c=c//10
        return x.next
