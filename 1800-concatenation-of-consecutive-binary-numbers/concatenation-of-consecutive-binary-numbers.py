class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        '''
        answer = 0
        curr_multiple = 1
        for i in range(n, 0, -1):
            answer += i * curr_multiple
            curr_multiple *= 2 ** (math.floor(math.log(i, 2)) + 1)
        return answer % MOD
        '''
        num_bits = 0
        answer = 0
        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                num_bits += 1
            answer = ((answer << num_bits) | i) % MOD
        return answer