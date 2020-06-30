# link :  https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head=sl=ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                sl.next=l1
                l1=l1.next
                sl=sl.next
            else:
                sl.next=l2
                l2=l2.next
                sl=sl.next
        sl.next=l1 or l2
        return head.next
