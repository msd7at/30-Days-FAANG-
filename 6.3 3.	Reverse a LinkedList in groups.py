#link:  https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/
class Solution:
    """

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return 
        cur=a=head
        prev=None
        stack=[]
        c=0
        while a:
            a=a.next
            c+=1
        
        while cur :
            val=0
            if c<k:
                while cur:
                    prev.next=ListNode(cur.val)
                    prev=prev.next
                    cur=cur.next
            else:
                while cur and val<k:
                    stack.append(cur.val)
                    cur=cur.next
                    val+=1
                    c-=1
                while stack:
                    if prev is None:
                        prev=ListNode(stack.pop())
                        head=prev
                    else:
                        prev.next=ListNode(stack.pop())
                        prev=prev.next
        prev.next=None
        return head
    """
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p = head
        e = r = ListNode(None)

        # find out the length of the list
        n = 0
        while head:
            head = head.next
            n += 1

        # rearrange the nodes
        for i in range(n // k):    # for every group
            s = p                  # record the first node of a group that will soon become the last node of the reversed group
            for _ in range(k):     # for every node in a group
                t = p.next
                p.next = e.next    # put the current node right before the head of the reversed group
                e.next = p         # register p as the head of the reversed group
                p = t              # visit the next node in the original list
            e = s                  # update the end of the reversed group
        e.next = p                 # append the tail to the end
        return r.next
