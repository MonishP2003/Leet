class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        filtered_bank = [row for row in bank if "1" in row]
        lasers = 0
        for i in range(len(filtered_bank)-1):
            lasers += filtered_bank[i].count("1") * filtered_bank[i + 1].count("1")
        return lasers