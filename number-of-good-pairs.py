class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = 0
        for i in dict(collections.Counter(nums)).values():
            n += i*(i-1)//2
        return n