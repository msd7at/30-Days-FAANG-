#link : https://leetcode.com/problems/linked-list-cycle-ii/
# explanation : https://leetcode.com/problems/linked-list-cycle-ii/discuss/715252/Python-3-2-pointers-Solution
class Solution:
   def detectCycle(self, head: ListNode) -> ListNode:
       slow=fast=head
       while fast and fast.next:
           slow=slow.next
           fast=fast.next.next
           if slow==fast:
               slow=head
               while slow:
                   if slow==fast:
                       return slow
                   slow=slow.next
                   fast=fast.next
       return None
