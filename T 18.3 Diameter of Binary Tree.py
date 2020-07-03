#LINK : https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.ans=1
        def hgt(root):
            if not root:
                return 0
            l=hgt(root.left)
            r=hgt(root.right)
            self.ans=max(self.ans,l+r+1)
            return max(l,r)+1
        hgt(root)
        return self.ans-1
        
