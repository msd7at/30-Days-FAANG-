# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol=[]
        def ans(root):
            if root :
                
                sol.append(root.val)
                ans(root.left)
                ans(root.right)
            else:
                return ans
        ans(root)
        return sol
