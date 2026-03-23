class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # Want to keep track of the most negative and most positive number
        dp = [[[float('inf'), float('-inf')] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        if grid[0][0] < 0:
            dp[0][0][0] = grid[0][0]
        elif grid[0][0] > 0:
            dp[0][0][1] = grid[0][0]
        else:
            return 0
        
        queue = deque()
        queue.append((0, 0))
        explored = set()
        while queue:
            i, j = queue.popleft()
            if (i, j) in explored:
                continue
            # Want to compute the best answer
            if i != 0 or j != 0:
                prev_answers = []
                if i > 0:
                    prev_answers.append(dp[i - 1][j][0])
                    prev_answers.append(dp[i - 1][j][1])
                if j > 0:
                    prev_answers.append(dp[i][j - 1][0])
                    prev_answers.append(dp[i][j - 1][1])
                
                for answer in prev_answers:
                    if answer == float('inf') or answer == float('-inf'):
                        continue
                    
                    if grid[i][j] == 0:
                        dp[i][j][0] = dp[i][j][1] = 0
                        continue
                    
                    if answer * grid[i][j] <= 0:
                        dp[i][j][0] = min(dp[i][j][0], answer * grid[i][j])
                    if answer * grid[i][j] >= 0:
                        dp[i][j][1] = max(dp[i][j][1], answer * grid[i][j])
                        
                
            if i < len(grid) - 1:
                queue.append((i + 1, j))
            if j < len(grid[0]) - 1:
                queue.append((i, j + 1))
            explored.add((i, j))
        if dp[-1][-1][1] == float('-inf'):
            return -1
        return dp[-1][-1][1] % (pow(10, 9) + 7)