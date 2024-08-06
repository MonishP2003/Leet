class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = 0
        for account in accounts:
            maxwealth = max(sum(account) , maxwealth)
        return maxwealth