class Solution:
    def minElement(self, nums: List[int]) -> int:
        answer = float('inf')
        for num in nums:
            curr = 0
            for char in str(num):
                curr += int(char)
            answer = min(answer, curr)
        return answer
