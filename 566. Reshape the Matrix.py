class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        oR=len(mat)
        oC=len(mat[0])
        if oR * oC != r*c:
            return mat
        idx=0
        res = [[0 for i in range(c)] for i in range(r)]
        for i in range(oR):
            for j in range(oC):
                res[idx//c][idx % c] = mat[i][j];
                idx += 1
        return res
