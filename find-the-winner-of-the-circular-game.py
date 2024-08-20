class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = 0

        for player in range(2,n+1):
            result = (result + k) % player
        return result + 1
        
   