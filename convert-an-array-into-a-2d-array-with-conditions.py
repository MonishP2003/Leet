class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = [[] for i in range(max(Counter(nums).values()))]
        for key, value in Counter(nums).items():
            for i in range(value):
                result[i].append(key)
        return result
