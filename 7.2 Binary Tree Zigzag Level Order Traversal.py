# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans=[]
        if not root:
            return ans
        def zlot(root,lev):
            if lev==len(ans):
                ans.append([])
            if lev % 2 == 0:
                ans[lev].append(root.val)
            else:
                ans[lev].insert(0,root.val)
            if root.left:
                zlot(root.left,lev+1)
            if root.right:
                zlot(root.right,lev+1)
        zlot(root,0)
        return ans
