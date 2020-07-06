# link :  https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            elif stack or root is None:
                root=stack.pop()
                ans.append(root.val)
                root=root.right
        return ans
        """
        ans=[]
        def iot(root):
            if not root:
                return None
            iot(root.left)
            ans.append(root.val)
            iot(root.right)
        iot(root)
        return ans
        """
