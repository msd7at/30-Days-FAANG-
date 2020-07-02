#link : - https://leetcode.com/problems/binary-tree-level-order-traversal/
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans=[]
        if not root :
            return ans
        def lot(root,level):
            if len(ans)==level:
                ans.append([])
            ans[level].append(root.val)
            if root.left :
                lot(root.left,level+1)
            if root.right:
                lot(root.right,level+1)
            
        lot(root,0)
        return ans
            
        
