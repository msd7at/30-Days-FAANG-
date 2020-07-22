# link :- https://leetcode.com/problems/sudoku-solver/
# explan: https://leetcode.com/problems/sudoku-solver/discuss/748258/Python-3-752ms-Soln-Backtracking
class Solution:
    def helper(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    for num in range(1,10):
                        num=str(num)
                        if self.isvalid(board,i,j,num):
                            board[i][j]=num
                            if self.helper(board):
                                return True
                            board[i][j]="."
                    return False
        return True
    def isvalid(self,board,row,col,num):
        for i in range(9):
            if board[i][col]==num:
                return False
            if board[row][i]==num:
                return False
            if board[3*(row//3) + i//3][ 3*(col//3)+i%3]==num:
                return False
        return True
                
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        return self.helper(board)
