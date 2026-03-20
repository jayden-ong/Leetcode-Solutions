class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        answer = []
        for i in range(len(grid) - k + 1):
            answer_row = []
            for j in range(len(grid[0]) - k + 1):
                curr_row = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        curr_row.append(grid[x][y])
                
                curr_answer = float('inf')
                curr_row.sort()
                for a in range(1, len(curr_row)):
                    if curr_row[a] == curr_row[a - 1]:
                        continue
                    
                    curr_answer = min(curr_answer, abs(curr_row[a] - curr_row[a - 1]))
                
                if curr_answer == float('inf'):
                    answer_row.append(0)
                else:
                    answer_row.append(curr_answer)

            answer.append(answer_row)
        return answer