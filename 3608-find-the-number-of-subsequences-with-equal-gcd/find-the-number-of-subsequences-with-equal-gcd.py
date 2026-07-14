class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        highest_gcd = max(nums)
        dp = [[0] * (highest_gcd + 1) for _ in range(highest_gcd + 1)]
        dp[0][0] = 1

        for num in nums:
            next_dp = [[0] * (highest_gcd + 1) for _ in range(highest_gcd + 1)]
            for i in range(highest_gcd + 1):
                divisor1 = math.gcd(i, num)
                for j in range(highest_gcd + 1):
                    curr = dp[i][j]
                    if curr == 0:
                        continue
                    
                    divisor2 = math.gcd(j, num)
                    next_dp[i][j] = (next_dp[i][j] + curr) % MOD
                    next_dp[divisor1][j] = (next_dp[divisor1][j] + curr) % MOD
                    next_dp[i][divisor2] = (next_dp[i][divisor2] + curr) % MOD
            dp = next_dp
        
        answer = 0
        for i in range(1, highest_gcd + 1):
            answer = (answer + dp[i][i]) % MOD
        return answer