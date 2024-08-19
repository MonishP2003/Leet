class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            subarray = sorted(nums[l[i]:r[i]+1])
            diff = subarray[1] - subarray[0]
            is_arithmetic = True
            for j in range(1,len(subarray)-1):
                if subarray[j+1] - subarray[j] != diff:
                    is_arithmetic = False
            result.append(is_arithmetic)
        return result
            