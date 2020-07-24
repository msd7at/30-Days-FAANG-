#link:  https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            i=inorder.index(postorder.pop())
            root=TreeNode(inorder[i])
            root.right=self.buildTree(inorder[i+1:],postorder)
            root.left=self.buildTree(inorder[:i],postorder)
            return root
