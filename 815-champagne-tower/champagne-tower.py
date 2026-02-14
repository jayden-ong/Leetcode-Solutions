class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(102)] for _ in range(102)]
        curr_row = 0
        dp[0][0] = poured
        while curr_row <= query_row:
            curr_glass = 0
            while curr_glass <= curr_row:
                split = (dp[curr_row][curr_glass] - 1) / 2
                if split > 0:
                    dp[curr_row + 1][curr_glass] += split
                    dp[curr_row + 1][curr_glass + 1] += split
                curr_glass += 1
            curr_row += 1

        return min(1, dp[query_row][query_glass])
