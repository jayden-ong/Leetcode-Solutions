from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        num_rows = len(grid)
        num_cols = num_rows
        # If the starting or ending spot is a thief, no safe path
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0 
        
        def is_valid(row, col):
            return row >= 0 and row < num_rows and col >= 0 and col < num_cols
        
        def bfs():
            safeness_factor_grid = [[float('inf')] * num_cols for _ in range(num_rows)]
            stack = deque()
            for i in range(num_rows):
                for j in range(num_cols):
                    if grid[i][j] == 1:
                        stack.append((i, j))
                        safeness_factor_grid[i][j] = 0
            
            # At each iteration, a new distance is being set for all the nodes in the stack
            while stack:
                curr_row, curr_col = stack.popleft()
                for direction in directions:
                    new_row, new_col = curr_row + direction[0], curr_col + direction[1]
                    if is_valid(new_row, new_col) and safeness_factor_grid[new_row][new_col] == float('inf'):
                        safeness_factor_grid[new_row][new_col] = safeness_factor_grid[curr_row][curr_col] + 1
                        stack.append((new_row, new_col))
            return safeness_factor_grid
        
        def safeness_helper(safeness_factor_grid):
            # Want to search by highest safety to guarantee the first time getting to a cell is the best possible safety
            heap = [(-safeness_factor_grid[0][0], 0, 0)]
            most_safe = [[-1] * num_rows for _ in range(num_rows)]
            # Want to store the best path to each tile
            most_safe[0][0] = safeness_factor_grid[0][0]
            # Remember that it is min heap, so make negative
            while heap:
                curr_safety, curr_row, curr_col = heapq.heappop(heap)
                curr_safety *= -1
                if curr_row == num_rows - 1 and curr_col == num_cols - 1:
                    return curr_safety

                for direction in directions:
                    new_row, new_col = curr_row + direction[0], curr_col + direction[1]
                    if is_valid(new_row, new_col):
                        new_safety = min(curr_safety, safeness_factor_grid[new_row][new_col])
                        # If the safety is better than it was, push it to queue
                        if new_safety > most_safe[new_row][new_col]:
                            most_safe[new_row][new_col] = new_safety
                            heapq.heappush(heap, (-new_safety, new_row, new_col))
            return -1

        safeness_factor_grid = bfs()
        return safeness_helper(safeness_factor_grid)
        
        
        

        return 0