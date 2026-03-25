class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        dp_row = []
        curr = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr += grid[i][j]
                if j == len(grid[0]) - 1:
                    dp_row.append(curr)
        
        if curr % 2 == 0:
            for i in range(len(dp_row) - 1):
                if curr // 2 == dp_row[i]:
                    return True
        
        dp_col = []
        curr = 0
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                curr += grid[i][j]
                if i == len(grid) - 1:
                    dp_col.append(curr)
        
        if curr % 2 == 0:
            for j in range(len(dp_col) - 1):
                if curr // 2 == dp_col[j]:
                    return True
        return False