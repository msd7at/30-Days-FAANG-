# link: https://leetcode.com/problems/binary-search-tree-iterator/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.q=[]
        self.AllLeftIntoStack(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        cur=self.q.pop()
        self.AllLeftIntoStack(cur.right)
        return cur.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.q!=[]
        
    def AllLeftIntoStack(self,root):
        while root:
            self.q.append(root)
            root=root.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
