class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        dp_coins = [[[float('-inf'), float('-inf'), float('-inf')] for _ in range(len(coins[0]))] for _ in range(len(coins))]
        dp_coins[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp_coins[0][0][1] = 0
        curr_queue = deque()
        curr_queue.append((0, 0))
        visited = set()
        while curr_queue:
            curr_row, curr_col = curr_queue.popleft()
            if (curr_row, curr_col) in visited:
                continue
            
            # Update current cell
            if curr_row != 0 or curr_col != 0:
                if curr_row > 0 and curr_col > 0:
                    most_coins = [max(dp_coins[curr_row][curr_col - 1][0], dp_coins[curr_row - 1][curr_col][0]), max(dp_coins[curr_row][curr_col - 1][1], dp_coins[curr_row - 1][curr_col][1]), max(dp_coins[curr_row][curr_col - 1][2], dp_coins[curr_row - 1][curr_col][2])]
                elif curr_row > 0:
                    most_coins = dp_coins[curr_row - 1][curr_col]
                else:
                    most_coins = dp_coins[curr_row][curr_col - 1]
                
                if coins[curr_row][curr_col] >= 0:
                    dp_coins[curr_row][curr_col] = [most_coins[0] + coins[curr_row][curr_col], most_coins[1] + coins[curr_row][curr_col], most_coins[2] + coins[curr_row][curr_col]]
                else:
                    dp_coins[curr_row][curr_col] = [most_coins[0] + coins[curr_row][curr_col], max(most_coins[0], most_coins[1] + coins[curr_row][curr_col]), max(most_coins[1], most_coins[2] + coins[curr_row][curr_col])]

            # Add cell below
            if curr_row < len(coins) - 1 and (curr_row + 1, curr_col) not in visited:
                curr_queue.append((curr_row + 1, curr_col))
            
            # Add cell to the right
            if curr_col < len(coins[0]) - 1 and (curr_row, curr_col + 1) not in visited:
                curr_queue.append((curr_row, curr_col + 1))
            
            visited.add((curr_row, curr_col))
        return max(dp_coins[-1][-1])