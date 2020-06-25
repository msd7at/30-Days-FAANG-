#link:-https://leetcode.com/problems/set-matrix-zeroes/
"""
timr c:-O(m*n)
space:-O(1)"""
class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        m=len(mat)
        n=len(mat[0])
        rc,cc=False,False
        for i in range(m):
            for j in range(n):
                if i==0 and mat[i][j]==0:
                    rc=True
                if j==0 and mat[i][j]==0:
                    cc=True
                if mat[i][j]==0:
                    mat[i][0]=0
                    mat[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if mat[0][j]==0 or mat[i][0]==0:
                    mat[i][j]=0
        if rc:
            for j in range(n):
                mat[0][j]=0
        if cc:
            for  i in range(m):
                mat[i][0]=0
        return mat
                    
                          
