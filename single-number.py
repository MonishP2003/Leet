from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict(Counter(nums))
        for i in d:
            if d[i] == 1:
                return i