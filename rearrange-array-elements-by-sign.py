class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = [i for i in nums if i > 0]
        n = [i for i in nums if i < 0]
        result = []
        for i in range(len(p)):
            result.append(p[i])
            result.append(n[i])
        return result