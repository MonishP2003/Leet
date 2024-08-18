class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1,m+1)]
        result = []
        for i in queries:
            if i in p:
                result.append(p.index(i))
                p.remove(i)
                p.insert(0,i)
        return result
