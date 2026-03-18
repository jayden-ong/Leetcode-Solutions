class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        prefix_sum = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = grid[i][j]
                if i > 0:
                    curr += prefix_sum[i - 1][j]
                
                if j > 0:
                    curr += prefix_sum[i][j - 1]
                
                if i > 0 and j > 0:
                    curr -= prefix_sum[i - 1][j - 1]
                
                prefix_sum[i][j] = curr
                if curr <= k:
                    answer += 1
        return answer