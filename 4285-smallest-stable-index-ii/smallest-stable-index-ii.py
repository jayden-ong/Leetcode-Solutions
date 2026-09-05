class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        mins = []
        curr_min = float('inf')
        for i in range(len(nums) - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            mins.append(curr_min)
        mins = mins[::-1]
        print(mins)
            
        curr_max = nums[0]
        curr_min = mins[0]
        for i in range(1, len(nums) + 1):
            if curr_max - curr_min <= k:
                return i - 1
            
            if i < len(nums):
                curr_max = max(curr_max, nums[i])
                curr_min = mins[i]
        return -1