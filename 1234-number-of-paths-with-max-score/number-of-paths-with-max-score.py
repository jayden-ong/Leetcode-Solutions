class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = pow(10, 9) + 7
        num_rows, num_cols = len(board), len(board[0])
        directions = [(0, -1), (-1, 0), (-1, -1)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < num_rows and 0 <= curr_col < num_cols
        
        dp = [[[0, 0] for _ in range(num_cols)] for _ in range(num_rows)]
        dp[-1][-1] = [0, 1]
        for curr_row in range(num_rows - 1, -1, -1):
            for curr_col in range(num_cols - 1, -1, -1):
                curr_state = dp[curr_row][curr_col]
                if board[curr_row][curr_col] == 'X' or curr_row == num_rows - 1 and curr_col == num_cols - 1:
                    continue
                
                for add_row, add_col in directions:
                    prev_row, prev_col = curr_row - add_row, curr_col - add_col
                    if not is_valid(prev_row, prev_col) or board[prev_row][prev_col] == 'X':
                        continue
                    
                    prev_state = dp[prev_row][prev_col]
                    if curr_state[0] < prev_state[0]:
                        curr_state[0], curr_state[1] = prev_state[0], prev_state[1]
                    elif curr_state[0] == prev_state[0]:
                        curr_state[1] += prev_state[1]
                
                if board[curr_row][curr_col] != 'E' and curr_state[1] > 0:
                    curr_state[0] += int(board[curr_row][curr_col])

        return [dp[0][0][0], dp[0][0][1] % MOD]