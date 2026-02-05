class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        answer = []
        for i, num in enumerate(nums):
            if num == 0:
                answer.append(num)
            elif num > 0:
                answer.append(nums[(i + num) % len(nums)])
            else:
                answer.append(nums[(i + len(nums) + num) % len(nums)])
        return answer