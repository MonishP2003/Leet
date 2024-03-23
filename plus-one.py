from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        while i >= -len(digits):
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                return digits
        digits.insert(0, 1)
        return digits
