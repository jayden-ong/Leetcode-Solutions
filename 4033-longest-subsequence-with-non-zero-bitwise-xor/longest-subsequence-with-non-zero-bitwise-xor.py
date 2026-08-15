class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        curr = 0
        for num in nums:
            curr ^= num
        
        if curr > 0:
            return len(nums)
        
        for num in nums:
            if curr ^ num > 0:
                return len(nums) - 1
        return 0