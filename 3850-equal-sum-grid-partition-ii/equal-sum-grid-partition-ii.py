class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # The connected condition only matters if an area is only one wide/long
        grid_set = defaultdict(int)
        dp_row = []
        dp_col = []
        curr = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr += grid[i][j]
                grid_set[grid[i][j]] += 1
            dp_row.append(curr)
        
        curr = 0
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                curr += grid[i][j]
            dp_col.append(curr)
        
        grid_set_up = defaultdict(int)
        grid_set_down = grid_set.copy()
        for i in range(len(grid) - 1):
            # See if it is possible without removing any elements
            if dp_row[len(grid) - 1] / 2 == dp_row[i]:
                return True

            desired_element = dp_row[len(grid) - 1] - 2 * dp_row[i]
            
            for j in range(len(grid[0])):
                grid_set_up[grid[i][j]] += 1
                grid_set_down[grid[i][j]] -= 1
            
            if desired_element < 0:
                # Only option is the corners if we are looking at the top row
                if (i == 0 and abs(desired_element) == grid[i][0] or abs(desired_element) == grid[i][len(grid[0]) - 1]) or (0 < i <= len(grid) - 2 and grid_set_up[abs(desired_element)] > 0 and (len(grid[0]) > 1 or grid[0][0] == abs(desired_element))):
                    return True
            else:
                if (i == len(grid) - 2 and abs(desired_element) == grid[i + 1][0] or abs(desired_element) == grid[i + 1][len(grid[0]) - 1]) or (0 <= i < len(grid) - 2 and grid_set_down[abs(desired_element)] > 0 and (len(grid[0]) > 1 or grid[len(grid) - 1][0] == abs(desired_element))):
                    return True

        grid_set_left = defaultdict(int)
        grid_set_right = grid_set.copy()
        for j in range(len(grid[0]) - 1):
            if dp_col[len(grid[0]) - 1] / 2 == dp_col[j]:
                return True
            
            desired_element = dp_col[len(grid[0]) - 1] - 2 * dp_col[j]
            
            for i in range(len(grid)):
                grid_set_left[grid[i][j]] += 1
                grid_set_right[grid[i][j]] -= 1
            #print(grid_set_left)
            #print(grid_set_right)
            #print(desired_element)
            if desired_element < 0:
                if (j == 0 and abs(desired_element) == grid[0][j] or abs(desired_element) == grid[len(grid) - 1][j]) or (0 < j <= len(grid[0]) - 2 and grid_set_left[abs(desired_element)] > 0 and (len(grid) > 1 or grid[0][0] == abs(desired_element))):
                    return True
            else:
                if (j == len(grid[0]) - 2 and abs(desired_element) == grid[0][j + 1] or abs(desired_element) == grid[len(grid) - 1][j + 1]) or (0 <= j < len(grid[0]) - 2 and grid_set_right[abs(desired_element)] > 0 and (len(grid) > 1 or grid[0][len(grid[0]) - 1] == abs(desired_element))):
                    return True
        return False
            
        