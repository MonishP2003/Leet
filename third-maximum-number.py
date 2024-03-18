from collections import Counter
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = sorted(list(Counter(nums).keys()))
        if len(n) > 2:
            return n[-3]
        elif len(n) == 2:
            return n[1]
        else:
            return n[0]
        
        