class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nums1 = []
        for i in range(0, len(nums)):
            nums1.append(nums[nums[i]])
        return nums1