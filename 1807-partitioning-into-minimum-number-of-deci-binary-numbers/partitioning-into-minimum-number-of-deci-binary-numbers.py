class Solution:
    def minPartitions(self, n: str) -> int:
        answer = float('-inf')
        for digit in n:
            answer = max(answer, int(digit))
        return answer