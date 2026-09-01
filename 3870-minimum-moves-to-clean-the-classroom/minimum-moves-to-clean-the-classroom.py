class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        start_row = start_col = 0
        num_litter = 0
        trash_pos = [[-1] * len(classroom[0]) for _ in range(len(classroom))]
        for row in range(len(classroom)):
            for col in range(len(classroom[0])):
                if classroom[row][col] == 'S':
                    start_row, start_col = row, col
                elif classroom[row][col] == 'L':
                    trash_pos[row][col] = num_litter
                    num_litter += 1
        
        if num_litter == 0:
            return 0
        
        trash_mask = (1 << num_litter) - 1

        best_energy = [[[-1] * (1 << num_litter) for _ in range(len(classroom[0]))] for _ in range(len(classroom))]
        queue = deque()

        best_energy[start_row][start_col][0] = energy
        queue.append((start_row, start_col, 0, energy, 0))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def is_valid(row, col):
            return 0 <= row < len(classroom) and 0 <= col < len(classroom[0])
        
        while queue:
            curr_row, curr_col, curr_mask, curr_energy, num_moves = queue.popleft()
            for add_row, add_col in directions:
                new_row, new_col = curr_row + add_row, curr_col + add_col
                if not is_valid(new_row, new_col) or classroom[new_row][new_col] == 'X' or curr_energy == 0:
                    continue
                
                new_mask = curr_mask
                new_energy = curr_energy - 1
                if classroom[new_row][new_col] == 'R':
                    new_energy = energy
                
                if classroom[new_row][new_col] == 'L':
                    new_mask |= 1 << trash_pos[new_row][new_col]
                
                if new_mask == trash_mask:
                    return num_moves + 1
                
                if new_energy <= best_energy[new_row][new_col][new_mask]:
                    continue
                
                best_energy[new_row][new_col][new_mask] = new_energy
                queue.append((new_row, new_col, new_mask, new_energy, num_moves + 1))
        return -1
