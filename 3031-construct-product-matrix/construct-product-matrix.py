class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        answer = [[0] * len(grid[0]) for _ in range(len(grid))]
        suffix = [[0] * len(grid[0]) for _ in range(len(grid))]
        final = 1
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                suffix[i][j] = final
                final = (final * grid[i][j]) % MOD
        
        curr = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer[i][j] = (curr * suffix[i][j]) % MOD
                curr = (curr * grid[i][j]) % MOD
        return answer