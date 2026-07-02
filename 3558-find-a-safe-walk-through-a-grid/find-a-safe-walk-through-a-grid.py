class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0])
        
        curr_health = health
        if grid[0][0] == 1:
            curr_health -= 1
        
        if curr_health == 0:
            return False
        
        heap, visited = [], set()
        heap.append((-curr_health, 0, 0))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited.add((0, 0))
        while heap:
            curr_health, curr_row, curr_col = heapq.heappop(heap)
            curr_health *= -1
            if curr_row == len(grid) - 1 and curr_col == len(grid[0]) - 1:
                return True
            
            for add_row, add_col in directions:
                new_row, new_col = curr_row + add_row, curr_col + add_col
                if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                    if curr_health == 1 and grid[new_row][new_col] == 1:
                        continue
                    
                    heapq.heappush(heap, (-curr_health + grid[new_row][new_col], new_row, new_col))
                    visited.add((new_row, new_col))

        return False