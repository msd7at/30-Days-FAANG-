class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        if m==0 :
            return
        n=len(board[0])
        if n==0:
            return
        def dfs(i,j,board):
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!="O":
                return 
            board[i][j]="#"
            dfs(i-1,j,board)
            dfs(i+1,j,board)
            dfs(i,j-1,board)
            dfs(i,j+1,board)
                
        for i in range(m):
            if board[i][0]=="O":
                dfs(i,0,board)
            if board[i][n-1]=="O":
                dfs(i,n-1,board)
        for i in range(n):
            if board[0][i]=="O":
              dfs(0,i,board)
            if board[m-1][i]=="O":
              dfs(m-1,i,board)
        
        for i in range(m):
          for j in range(n):
            if board[i][j]=="O":
              board[i][j]="X"
            elif board[i][j]=="#":
              board[i][j]="O"
              
                
            
            
