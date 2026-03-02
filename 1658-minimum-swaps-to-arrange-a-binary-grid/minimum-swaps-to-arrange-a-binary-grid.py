class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # Need to find a row that has n - 1 0's at the end, n - 2 0's at the end, and so on.
        # It doesn't matter what the last row is, so we can ignore index 0 of "rows_needed"
        # Want to map each row number to where each row currently is
        list_to_sort = []
        for i, row in enumerate(grid):
            num_zeros = 0
            for num in row:
                if num == 0:
                    num_zeros += 1
                else:
                    num_zeros = 0
            
            list_to_sort.append(num_zeros)
        
        # There are two possibilities for the bottom row
        #   There is a row with 0 0s above the diagonal -- it becomes the last row
        #   There are two rows with the same number of zeros -- the larger row becomes the last row
        # print(desired_row_to_row)
        answer = 0
        for i in range(len(list_to_sort)):
            if list_to_sort[i] >= len(grid) - i - 1:
                continue
            
            chosen = None
            for j in range(i + 1, len(grid)):
                if list_to_sort[j] >= len(grid) - i - 1:
                    chosen = j
                    break
            
            if not chosen:
                return -1
            
            for j in range(chosen, i, -1):
                list_to_sort[j], list_to_sort[j - 1] = list_to_sort[j - 1], list_to_sort[j]
                answer += 1
        
        return answer