class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][len(t)] = 1
        
        for j in range(len(s) - 1, -1, -1):
            for k in range(len(t) - 1, -1, -1):
                # no matter what, our answer is at least the previous answer (skipping this char)
                dp[j][k] = dp[j + 1][k]
                if s[j] == t[k]:
                    dp[j][k] += dp[j + 1][k + 1]
        return dp[0][0]
            

