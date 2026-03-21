class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for j in range(y, y + k):
            for i in range(x, (x + k + x) // 2):
                grid[i][j], grid[x + k - 1 - i + x][j] = grid[x + k - 1 - i + x][j], grid[i][j]
        return grid