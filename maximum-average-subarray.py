class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        msum = sum1 = sum(nums[0:k])
        print(msum)
        for i in range(k,len(nums)):
            sum1 += nums[i] - nums[i - k]
            msum = max(msum, sum1)
        return msum/k