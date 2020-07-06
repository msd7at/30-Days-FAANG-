# link : https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]: 
	    ans = []
	    stack = [root]
	    while stack:
		    root = stack.pop()
		    if root: 
			    ans.append(root.val)
			    stack += [root.left, root.right]
	    return ans[::-1]
                
    """
        ans=[]
        def iot(root):
            if not root:
                return None
            iot(root.left)
            iot(root.right)
            ans.append(root.val)
        iot(root)
        return ans
        """
