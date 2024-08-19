class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m,n = len(rowSum), len(colSum)
        result = [[0] * n for i in range(m)]

        i,j = m-1,n-1

        while i >= 0 and j >= 0:
            if rowSum[i] <= colSum[j]:
                result[i][j] = rowSum[i]
                colSum[j] -= rowSum[i]
                i -= 1
            else:
                result[i][j] = colSum[j]
                rowSum[i] -= colSum[j]
                j -= 1
        return result
