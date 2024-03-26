class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        elif len(nums) == 1:
            return nums[0]
        
        else:
            l =[0]*(len(nums)+1)
            l[0] = nums[0]
            l[1] = max(nums[0], nums[1])
            print(l)
            for i in range(2, len(nums)):
                l[i] = max(l[i - 2] + nums[i], l[i - 1])
                print(l)
            return l[len(nums)-1]