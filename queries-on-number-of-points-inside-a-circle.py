class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        l = []
        for i in queries:
            c = 0
            for j in points:
                if sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2) <= i[2]:
                    c+=1
            l.append(c)
        return l