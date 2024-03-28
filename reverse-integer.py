class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        if x > 0:
            n = int(str(x)[::-1])
        else:
            n = int(str(x * -1)[::-1]) * -1
        
        if n < (-2**31) or n > (2**31 - 1):
            return 0
        return n