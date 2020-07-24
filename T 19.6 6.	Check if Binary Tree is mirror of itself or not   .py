# link :  https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def sys(L,R):
            if not L and not R:
                return True
            if L and R and L.val==R.val:
                return sys(L.left,R.right) and sys(L.right,R.left)
            return False
        return sys(root,root)
