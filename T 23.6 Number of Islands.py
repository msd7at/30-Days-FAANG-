# link: https://leetcode.com/problems/number-of-islands/

class Solution:
    def dfs(self,grid,i,j):
        if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]=="0":
            return
        grid[i][j]="0"
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i+1,j)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    count+=1
        return count
