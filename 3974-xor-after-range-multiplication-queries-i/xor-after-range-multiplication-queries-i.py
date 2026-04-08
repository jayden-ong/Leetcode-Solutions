class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7
        for left, right, skip, multiply in queries:
            for i in range(left, right + 1, skip):
                nums[i] = (nums[i] * multiply) % MOD

        answer = nums[0]
        for i in range(1, len(nums)):
            answer ^= nums[i]
        return answer