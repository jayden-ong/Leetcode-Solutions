class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Want to take the largest element and increment everything except for it
        # Take the sum of the elements and divide by number of elements
        if nums == [nums[0]] * len(nums):
            return 0
        
        # sum of nums = 6 -> 8 -> 10 -> 12
        # curr_length = 3
        smallest = min(nums)
        answer = 0
        for num in nums:
            answer += num - smallest
        return answer