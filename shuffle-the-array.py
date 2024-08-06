class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1 = []
        for i in range(len(nums) - n):
            l1.append(nums[i])
            l1.append(nums[n + i])
        return l1