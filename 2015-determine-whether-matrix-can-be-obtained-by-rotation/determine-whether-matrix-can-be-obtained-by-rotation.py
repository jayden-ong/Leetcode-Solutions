class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        num_rows_cols = len(mat)
        def rotate(matrix):
            answer = []
            for j in range(num_rows_cols - 1, -1, -1):
                new_row = []
                for i in range(num_rows_cols):
                    new_row.append(matrix[i][j])
                answer.append(new_row)
            return answer
        
        def custom_check(matrix, target):
            for i in range(num_rows_cols):
                for j in range(num_rows_cols):
                    if matrix[i][j] != target[i][j]:
                        return False

            return True
        
        curr = mat
        for i in range(4):
            #print(curr)
            if custom_check(curr, target):
                return True
            curr = rotate(curr)
        
        return False