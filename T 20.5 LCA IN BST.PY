# LINK : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lca(self,root,p,q):
        if p.val < root.val and q.val <root.val:
            return self.lca(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lca(root.right,p,q)
        return root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        return self.lca(root,p,q)
