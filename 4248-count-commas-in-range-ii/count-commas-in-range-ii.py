class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        curr = 1000
        answer = 0
        num_commas = 1
        while n >= curr:
            answer += (min(1000 * curr, n + 1) - curr) * num_commas
            curr *= 1000
            num_commas += 1
        return answer
