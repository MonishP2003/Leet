from collections import Counter
import functools
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return functools.reduce(gcd, Counter(deck).values()) > 1

Solution()      