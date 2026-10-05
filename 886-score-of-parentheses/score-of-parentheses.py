class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        answer = 0
        counter = 0
        for i, char in enumerate(s):
            if char == "(":
                counter += 1
            else: 
                counter -= 1
                if s[i - 1] == "(":
                    answer += pow(2, counter)
        return answer