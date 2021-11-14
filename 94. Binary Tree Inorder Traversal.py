# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol=[]
        def ans(root):
            if root :
                ans(root.left)
                sol.append(root.val)
                ans(root.right)
            else:
                return ans
        ans(root)
        return sol
