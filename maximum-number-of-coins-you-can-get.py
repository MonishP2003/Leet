class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maxcoins = 0

        for i in range(len(piles)//3,len(piles),2):
            maxcoins += piles[i]

        return maxcoins