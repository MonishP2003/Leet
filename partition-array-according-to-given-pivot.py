class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l1 = [num for num in nums if num < pivot]
        l2 = [num for num in nums if num == pivot]
        l3 = [num for num in nums if num > pivot]
        return l1 + l2 + l3