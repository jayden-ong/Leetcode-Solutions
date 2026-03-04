class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Count number of 1s in a row
        num_rows = len(mat)
        num_cols = len(mat[0])
        row_cand = [-1] * num_rows
        col_sum = [0] * num_cols
        for i in range(num_rows):
            num_ones_in_row = 0
            curr_cand = -1
            for j in range(num_cols):
                # Count 1s in row
                if mat[i][j] == 1:
                    num_ones_in_row += 1
                    curr_cand = j
                    col_sum[j] += 1
            
            if num_ones_in_row == 1:
                row_cand[i] = curr_cand
        
        answer = 0
        #print(row_cand)
        #print(col_sum)
        for cand in row_cand:
            if cand != -1 and col_sum[cand] == 1:
                answer += 1
        return answer