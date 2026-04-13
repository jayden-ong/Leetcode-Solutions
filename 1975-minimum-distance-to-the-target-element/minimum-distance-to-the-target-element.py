class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        num_nums = len(nums)
        answer = float('inf')
        for i in range(num_nums):
            if nums[i] == target:
                answer = min(answer, abs(i - start))
        return answer