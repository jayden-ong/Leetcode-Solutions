class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        answer = [float('-inf'), float('-inf'), float('-inf')]
        def determine_candidates(curr_answer, candidate):
            if candidate == curr_answer[0] or candidate == curr_answer[1] or candidate == curr_answer[2]:
                return 
            if candidate > curr_answer[0]:
                curr_answer[0], curr_answer[1], curr_answer[2] = candidate, curr_answer[0], curr_answer[1]
            elif candidate > curr_answer[1]:
                curr_answer[1], curr_answer[2] = candidate, curr_answer[1]
            elif candidate > curr_answer[2]:
                curr_answer[2] = candidate
            
        prefix_sum = [[[0, 0] for _ in range(len(grid[0]) + 2)] for _ in range(len(grid) + 1)]

        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                prefix_sum[i][j][0] = prefix_sum[i - 1][j - 1][0] + grid[i - 1][j - 1]
                prefix_sum[i][j][1] = prefix_sum[i - 1][j + 1][1] + grid[i - 1][j - 1]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                determine_candidates(answer, grid[i][j])
                for k in range(i + 2, len(grid), 2):
                    u1, u2 = i, j
                    d1, d2 = k, j
                    l1, l2 = (i + k) // 2, j - (k - i) // 2
                    r1, r2 = (i + k) // 2, j + (k - i) // 2

                    if l2 < 0 or r2 >= len(grid[0]):
                        break
                    
                    candidate = (prefix_sum[l1 + 1][l2 + 1][1] - prefix_sum[u1][u2 + 2][1]) + (prefix_sum[r1 + 1][r2 + 1][0] - prefix_sum[u1][u2][0]) +(prefix_sum[d1 + 1][d2 + 1][0] - prefix_sum[l1][l2][0]) + (prefix_sum[d1 + 1][d2 + 1][1] - prefix_sum[r1][r2 + 2][1]) - (grid[u1][u2] + grid[d1][d2] + grid[l1][l2] + grid[r1][r2])
                    determine_candidates(answer, candidate)
        if answer[1] == float('-inf'):
            return [answer[0]]
        elif answer[2] == float('-inf'):
            return [answer[0], answer[1]]
        return answer