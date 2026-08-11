class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        max_sum = nums[0]
        i = 1
        while i < len(nums):
            if nums[i - 1] + 1 == nums[i]:
                max_sum += nums[i]
            else:
                break
            i += 1
        
        curr_num = max_sum
        nums_set = set(nums)
        while curr_num in nums_set:
            curr_num += 1
        return curr_num