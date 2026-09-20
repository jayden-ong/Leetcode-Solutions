class Solution:
    def reverseDegree(self, s: str) -> int:
        answer = 0
        for i, char in enumerate(s):
            answer += (26 - (ord(char) - ord('a'))) * (i + 1)
        return answer