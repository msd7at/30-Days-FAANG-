#  link  https://leetcode.com/problems/binary-tree-preorder-traversal/
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                ans.append(root.val)
                root=root.left
            elif stack or root is None:
                root=stack.pop()
                root=root.right
        return ans
        """
        ans=[]
        def iot(root):
            if not root:
                return None
            ans.append(root.val)
            iot(root.left)
            iot(root.right)
        iot(root)
        return ans
        """
