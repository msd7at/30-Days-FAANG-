# LINK :  https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root:
            l=self.maxDepth(root.left)
            r=self.maxDepth(root.right)
            if r>l:
                return r+1
            else:
                return l+1
