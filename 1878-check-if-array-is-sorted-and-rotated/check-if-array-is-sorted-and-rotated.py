class Solution:
    def check(self, nums: List[int]) -> bool:
        nums_copy = nums.copy()
        nums_copy.sort()
        start_point = None
        for i in range(len(nums)):
            if nums[i:] + nums[:i] == nums_copy[:]:
                return True
        return False
