class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0
            
        curr_max = nums[0]
        curr_min = min(nums)
        for i in range(1, len(nums) + 1):
            if curr_max - curr_min <= k:
                return i - 1
            
            if i < len(nums):
                curr_max = max(curr_max, nums[i])
                curr_min = min(nums[i:])
        return -1