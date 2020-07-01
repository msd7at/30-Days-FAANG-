# link https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=cur=ListNode(0)
        carry=0
        while l1 or l2 or carry:
            if l1:
                carry=carry+l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            cur.next=ListNode(carry%10)
            cur=cur.next
            carry=carry//10
        return dummy.next
