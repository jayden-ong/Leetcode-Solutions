class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = pow(10, 9) + 7
        num_vals = r - l + 1
        # How many numbers are less than "i".
        # Answer : i - l
        # How many numbers are greater than "i"
        # Answer : r - i
        dp_down = [1] * num_vals
        dp_up = [1] * num_vals
        for _ in range(n - 1):
            sum0, sum1 = list(accumulate(dp_down, initial=0)), list(accumulate(dp_up, initial=0))
            dp_down = [x % MOD for x in sum1[:-1]]

            sum_down = sum0[-1]
            dp_up = [(sum_down - x) % MOD for x in sum0[1:]]
        return (sum(dp_down) + sum(dp_up)) % MOD
