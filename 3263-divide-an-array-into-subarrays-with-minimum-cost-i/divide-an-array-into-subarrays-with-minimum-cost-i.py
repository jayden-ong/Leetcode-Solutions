class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_cost = nums[0]
        smallest = float('inf')
        second_smallest = float('inf')
        for i in range(1, len(nums)):
            if nums[i] < smallest:
                second_smallest = smallest
                smallest = nums[i]
            elif nums[i] < second_smallest:
                second_smallest = nums[i]
        return first_cost + smallest + second_smallest