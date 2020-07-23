#link https://leetcode.com/problems/binary-tree-maximum-path-sum/
# explanation : https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/751753/Python-3-Faster-than-91
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def mpu(root):
            if not root:
                return 0
            left=mpu(root.left)
            right=mpu(root.right)
            ms=max(max(left,right)+root.val,root.val)
            m21=max(ms,left+right+root.val)
            self.res=max(self.res,m21)

            return ms
        self.res=float('-inf')
        mpu(root)
        return self.res
