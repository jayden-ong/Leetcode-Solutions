class Solution:
    def sumAndMultiply(self, n: int) -> int:
        curr_sum = 0
        curr_answer = ""
        for digit in str(n):
            if digit == '0':
                continue
            curr_answer += digit
            curr_sum += int(digit)
        
        if curr_answer == "":
            return 0
        return int(curr_answer) * curr_sum