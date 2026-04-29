class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
        
        prefix_sum_grid = [[0 for _ in range(n)] for _ in range(n + 1)]
        for j in range(n):
            for i in range(1, n + 1):
                prefix_sum_grid[i][j] = prefix_sum_grid[i - 1][j] + grid[i - 1][j]

        dp = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n)]
        prev_max = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        prev_suff_max = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for j in range(1, n):
            for curr_h in range(n + 1):
                for prev_h in range(n + 1):
                    # Every value left in the column gets added as part of optimal score
                    if curr_h <= prev_h:
                        additional_score = prefix_sum_grid[prev_h][j] - prefix_sum_grid[curr_h][j]
                        dp[j][curr_h][prev_h] = max(dp[j][curr_h][prev_h], prev_suff_max[prev_h][0] + additional_score)
                    # Every value adjacent to the left gets added
                    else:
                        additional_score = prefix_sum_grid[curr_h][j - 1] - prefix_sum_grid[prev_h][j - 1]
                        dp[j][curr_h][prev_h] = max(dp[j][curr_h][prev_h], prev_suff_max[prev_h][curr_h], prev_max[prev_h][curr_h] + additional_score)
            
            for curr_h in range(n + 1):
                prev_max[curr_h][0] = dp[j][curr_h][0]
                for prev_h in range(1, n + 1):
                    penalty = 0
                    if prev_h > curr_h:
                        penalty = prefix_sum_grid[prev_h][j] - prefix_sum_grid[curr_h][j]
                    prev_max[curr_h][prev_h] = max(prev_max[curr_h][prev_h - 1], dp[j][curr_h][prev_h] - penalty)

                prev_suff_max[curr_h][n] = dp[j][curr_h][n]
                for prev_h in range(n - 1, -1, -1):
                    prev_suff_max[curr_h][prev_h] = max(prev_suff_max[curr_h][prev_h + 1], dp[j][curr_h][prev_h])
        
        answer = 0
        for k in range(n + 1):
            answer = max(answer, dp[n - 1][n][k], dp[n - 1][0][k])
        return answer

