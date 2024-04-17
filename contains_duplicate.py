from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in Counter(nums).values():
            if i > 1:
                return True
        return False