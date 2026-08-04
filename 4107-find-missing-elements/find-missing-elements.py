class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        answer = []
        for i in range(min(nums), max(nums) + 1):
            if i not in nums_set:
                answer.append(i)
        return answer