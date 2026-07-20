class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # After num_rows * num_cols shifts, back to normal
        num_rows = len(grid)
        num_cols = len(grid[0])
        actual_shift = k % (num_rows * num_cols)
        if actual_shift == 0:
            return grid
        # num_cols - actual shift columns will be translated to the right
        # actual_shift // num_cols indicates how many times the rows have rotated
        stopping_point = num_rows - (actual_shift // num_cols)
        new_grid = grid[stopping_point:] + grid[:stopping_point]
        num_shifts = actual_shift % num_cols
        answer = []
        for i in range(num_rows):
            if i == 0:
                # These will be the last columns
                answer.append(new_grid[-1][num_cols - num_shifts:] + new_grid[i][:num_cols - num_shifts])
            else:
                answer.append(new_grid[i - 1][num_cols - num_shifts:] + new_grid[i][:num_cols - num_shifts])
        return answer