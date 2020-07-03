""" Method 1 """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def height(root):
            if not root:
                return 0
            return max(height(root.left),height(root.right))+1
        l=height(root.left)
        r=height(root.right)
        if abs(l-r) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right) :
            return True
        return False
 
 """ Method 2 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def bal(root):
            if not root:
                return 0
            l=bal(root.left)
            r=bal(root.right)
            if l is False or r is False:
                return False
            if abs(l-r)>1:
                return False
            return max(l,r)+1
        
        return bal(root)
        
