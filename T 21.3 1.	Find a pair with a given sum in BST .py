#link:  https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
#explanation:  https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/757627/Python-3-Two-Solution-i)-using-set-ii)-BST
#1-Set

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.target=k
        self.add=set()
        self.aa=False
        self.rec(root)
        return self.aa
    def rec(self,root):
        if not root:
            return 
        self.rec(root.left)
        if self.target - root.val in self.add:
            self.aa=True
            return 
        self.add.add(root.val)
        self.rec(root.right)
#2-BST

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.l=[]
        self.rec(root)
        low=0
        high=len(self.l)-1
        while low<high:
            if self.l[low]+self.l[high]==k:
                return True
            elif self.l[low]+self.l[high]<k:
                low+=1
            else:
                high-=1
        return False
    def rec(self,root):
        if not root:
            return
        self.rec(root.left)
        self.l.append(root.val)
        self.rec(root.right)
