#link:  https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root,float("-inf"),float("inf"))
    
    def helper(self,root,low,high):
        if not root:
            return True
        if not root.left and not root.right:
            return low<root.val<high
        return low < root.val < high and self.helper(root.left,low,root.val) and self.helper(root.right,root.val,high)
