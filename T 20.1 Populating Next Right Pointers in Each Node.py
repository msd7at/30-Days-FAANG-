# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None :
            return root
        q=deque([root])
        while q:
            size=len(q)
            while size>0:
                node=q.popleft()
                if size>1:
                    node.next=q[0]
                size-=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
