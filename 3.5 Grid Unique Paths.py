link:- https://leetcode.com/problems/unique-paths/
Explanation:- https://leetcode.com/problems/unique-paths/discuss/669770/Python-Faster-than-94-DP-easy-Explanation
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l=[]
        for i in range(m):
            s=[]
            for j in range(n):
                s.append(0)
            l.append(s)
        for i in range(m):
            l[i][0]=1
        for j in range(n):
            l[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                l[i][j]=l[i-1][j]+l[i][j-1]
        return l[m-1][n-1]
