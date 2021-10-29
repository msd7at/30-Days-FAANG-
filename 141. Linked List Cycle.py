# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=b=head
        if not head or not head.next:
            return False
        while b.next and b.next.next:
            a=a.next
            b=b.next.next
            if a==b:
                return True
        return False
