MOD, MAX = 1000000007, 100001
pow = [1] * MAX
for i in range(1, MAX):
    pow[i] = (pow[i - 1] * 10) % MOD
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        '''
        MOD = pow(10, 9) + 7
        curr_digits_int, prefix_digits_int = 0, []
        prefix_sum = []
        curr_sum = 0
        curr_length, prefix_length = 0, []
        ten_pows = [1] * len(s)
        for i in range(1, len(s)):
            ten_pows[i] = (ten_pows[i - 1] * 10) % MOD
        
        for digit in s:
            if digit != "0":
                curr_sum += int(digit)
                curr_digits_int = (curr_digits_int * 10 + int(digit))
                curr_length += 1
            prefix_sum.append(curr_sum)
            prefix_digits_int.append(curr_digits_int)
            prefix_length.append(curr_length)

        answer = []
        for left, right in queries:
            if left == 0:
                answer.append((prefix_digits_int[right] * prefix_sum[right]) % MOD)
            else:
                curr_sum = prefix_sum[right] - prefix_sum[left - 1]
                diff_in_lengths = prefix_length[right] - prefix_length[left - 1]
                digits_multiple = (prefix_digits_int[right] - prefix_digits_int[left - 1] * ten_pows[diff_in_lengths])
                answer.append((digits_multiple * curr_sum) % MOD)
        return answer
        '''
        n, res = len(s), []
        A, B, Len = [[0] * (n + 1) for _ in range(3)]

        for i in range(n):
            d = int(s[i])
            A[i + 1] = A[i] + d
            B[i + 1] = (B[i] * 10 + d) % MOD if d else B[i]
            Len[i + 1] = Len[i] + (d > 0)

        res = []

        for l, r in queries:
            r += 1

            sub = (B[l] * pow[Len[r] - Len[l]]) % MOD
            x = (B[r] - sub) % MOD

            res.append((x * (A[r] - A[l])) % MOD)

        return res