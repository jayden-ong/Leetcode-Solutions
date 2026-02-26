import math
class Solution:
    def numSteps(self, s: str) -> int:
        curr_num = 0
        for i in range(len(s) - 1, -1, -1):
            curr_power = len(s) - 1 - i
            curr_num += int(s[i]) * pow(2, curr_power)
        
        answer = 0
        while curr_num != 1:
            if curr_num % 2 == 1:
                curr_num //= 2
                curr_num += 1
                answer += 2
            else:
                if (curr_num & (curr_num - 1)) == 0:
                    return answer + int(math.log2(curr_num))
                curr_num //= 2
                answer += 1
        return answer
