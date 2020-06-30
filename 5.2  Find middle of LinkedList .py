#link :  https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return 
        s=head
        e=head
        while e and e.next:
            s=s.next
            e=e.next.next
        if e and e.next:
            s=s.next
        print(s.val)
        return s

        
        
