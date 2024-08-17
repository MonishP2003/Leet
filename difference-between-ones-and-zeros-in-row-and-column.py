class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        row = [0] * m
        col = [0] * n
        
        for i in range(m):
            for j in range(n):
                row[i] += 1 if grid[i][j] == 1 else -1
                col[j] += 1 if grid[i][j] == 1 else -1

        diff = [[row[i] + col[j] for j in range(n)] for i in range(m)]

        return diff