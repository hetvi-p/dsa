class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = -1 
        total = 0
        res = float("inf")

        for i in range(len(nums)):

            if nums[i] >= target:
                return 1

            nums[i] += total 
            total = nums[i]

            while nums[i] - (0 if left == -1 else nums[left]) >= target:
                res = min(i - left, res)
                left += 1
        
        return 0 if  res == float("inf") else res

