# link    https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None :
            return True
        if p and q:
            return (p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        return False
