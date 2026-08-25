class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        for i in range(k, (len(nums) + 1) * k, k):
            if i not in nums_set:
                return i
        return (len(nums) + 1) * k