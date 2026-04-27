class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        visited = set()
        cells_queue = deque()
        left_streets, right_streets, up_streets, down_streets = {1, 3, 5}, {1, 4, 6}, {2, 5, 6}, {2, 3, 4}
        cells_queue.append((0, 0))
        street_to_new_direction = {("left", 1) : "right", ("left", 3) : "down", ("left", 5) : "up",
                                  ("right", 1) : "left", ("right", 4) : "down", ("right", 6) : "up",
                                  ("up", 2) : "down", ("up", 5) : "left", ("up", 6) : "right",
                                  ("down", 2) : "up", ("down", 3) : "left", ("down", 4) : "right",
                                  }
        while cells_queue:
            curr_row, curr_col = cells_queue.popleft()
            if curr_row == len(grid) - 1 and curr_col == len(grid[0]) - 1:
                return True
            
            curr_street = grid[curr_row][curr_col]
            if curr_street == 4 and curr_row == 0 and curr_col == 0:
                if curr_row + 1 < len(grid) and grid[curr_row + 1][curr_col] in up_streets:
                    cells_queue.append((curr_row + 1, curr_col))
                if curr_col + 1 < len(grid[0]):
                    cells_queue.append((curr_row, curr_col + 1))
                visited.add((0, 0))
                continue
            
            if curr_street in left_streets:
                if curr_col - 1 >= 0 and (curr_row, curr_col - 1) not in visited and grid[curr_row][curr_col - 1] in right_streets:
                    cells_queue.append((curr_row, curr_col - 1))
            
            if curr_street in right_streets:
                if curr_col + 1 < len(grid[0]) and (curr_row, curr_col + 1) not in visited and grid[curr_row][curr_col + 1] in left_streets:
                    cells_queue.append((curr_row, curr_col + 1))

            if curr_street in up_streets:
                if curr_row - 1 >= 0 and (curr_row - 1, curr_col) not in visited and grid[curr_row - 1][curr_col] in down_streets:
                    cells_queue.append((curr_row - 1, curr_col))

            if curr_street in down_streets:
                if curr_row + 1 < len(grid) and (curr_row + 1, curr_col) not in visited and grid[curr_row + 1][curr_col] in up_streets:
                    cells_queue.append((curr_row + 1, curr_col))

            visited.add((curr_row, curr_col))
        return False