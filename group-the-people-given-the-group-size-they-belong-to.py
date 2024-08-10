class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        l = []
        g = {}
        for i, size in enumerate(groupSizes):
            if size not in g:
                g[size] = []
            g[size].append(i)
            
            if len(g[size]) == size:
                l.append(g[size])
                g[size] = []
        return l