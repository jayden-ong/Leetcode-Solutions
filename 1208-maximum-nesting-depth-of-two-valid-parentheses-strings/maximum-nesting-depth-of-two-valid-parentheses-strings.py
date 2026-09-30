class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = []
        curr_depth = 0
        for char in seq:
            if char == "(":
                curr_depth += 1
                answer.append(curr_depth % 2)
            elif char == ")":
                answer.append(curr_depth % 2)
                curr_depth -= 1
            
        return answer