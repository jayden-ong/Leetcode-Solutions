class Solution:
    def maxDepth(self, s: str) -> int:
        answer = 0
        curr = 0
        for char in s:
            if char == "(":
                curr += 1
                answer = max(answer, curr)
            elif char == ")":
                curr -= 1
        return answer