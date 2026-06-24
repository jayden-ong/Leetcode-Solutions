class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = pow(10, 9) + 7

        def multiply(matrix1, matrix2):
            n, m = len(matrix1), len(matrix2[0])
            answer = [[0] * m for _ in range(n)]

            for i in range(n):
                for k in range(len(matrix1[0])):
                    right = matrix1[i][k]
                    if right == 0:
                        continue
                    for j in range(m):
                        answer[i][j] = (answer[i][j] + right * matrix2[k][j]) % MOD
            return answer
        
        def fast_exp(base, exponent, answer):
            while exponent > 0:
                if exponent & 1:
                    answer = multiply(answer, base)
                base = multiply(base, base)
                exponent >>= 1
            return answer

        num_vals = r - l + 1
        if n == 1:
            return num_vals
        
        matrix = [[0] * (num_vals * 2) for _ in range(num_vals * 2)]
        for i in range(num_vals):
            for j in range(i):
                matrix[i][j + num_vals] = 1
            for j in range(i + 1, num_vals):
                matrix[i + num_vals][j] = 1

        dp = [[1] * (num_vals * 2)]
        dp = fast_exp(matrix, n - 1, dp)
        answer = 0
        for i in range(num_vals * 2):
            answer = (answer + dp[0][i]) % MOD
        return answer