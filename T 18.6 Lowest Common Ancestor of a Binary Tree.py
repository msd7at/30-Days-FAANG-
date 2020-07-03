# Link   https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root is p or root is q:
            return root
        llca=self.lowestCommonAncestor(root.left,p,q)
        rrca=self.lowestCommonAncestor(root.right,p,q)
        
        if llca and rrca :
            return root
        if llca is not None:
            return llca
        else:
            return rrca
