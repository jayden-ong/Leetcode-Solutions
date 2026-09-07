class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = pow(10, 9) + 7
        dp = [1]
        prev_occur = {}
        for i, char in enumerate(s):
            dp.append(dp[-1] * 2)
            if char in prev_occur:
                dp[-1] -= dp[prev_occur[char]]
            prev_occur[char] = i
        return (dp[-1] - 1) % MOD