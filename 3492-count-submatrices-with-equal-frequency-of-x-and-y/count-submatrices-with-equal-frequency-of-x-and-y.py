class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        prefix = [[[0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "X":
                    prefix[i][j][0] += 1
                elif grid[i][j] == "Y":
                    prefix[i][j][1] += 1
                    
                if i > 0:
                    prefix[i][j][0] += prefix[i - 1][j][0]
                    prefix[i][j][1] += prefix[i - 1][j][1]  
                if j > 0:
                    prefix[i][j][0] += prefix[i][j - 1][0]
                    prefix[i][j][1] += prefix[i][j - 1][1]
                if i > 0 and j > 0:
                    prefix[i][j][0] -= prefix[i - 1][j - 1][0]
                    prefix[i][j][1] -= prefix[i - 1][j - 1][1]
                
                if prefix[i][j][0] > 0 and prefix[i][j][0] == prefix[i][j][1]:
                    answer += 1
        return answer