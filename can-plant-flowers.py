class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c, prev = 0, 0
        
        for cur in flowerbed:
            if cur == 1:
                if prev == 1:
                    c -= 1
                prev = cur
            else:
                if prev == 1:
                    prev = cur
                else:
                    c += 1
                    prev = 1
        return c >= n