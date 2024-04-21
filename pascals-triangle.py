class Solution:
    def generate(self, n: int) -> List[List[int]]:
        o = []
        if n == 0:
            return []
        if n >= 1:
            o.append([1])
        if n >= 2:
            o.append([1, 1])
        for i in range(2, n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = o[i - 1][j - 1] + o[i - 1][j]
            o.append(row)
        return o
