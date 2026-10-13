class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums_squared = []
        for num in nums:
            nums_squared.append(num ** 2)
        nums_squared.sort()
        return sum(nums_squared[len(nums) // 2:]) - sum(nums_squared[:len(nums) // 2])