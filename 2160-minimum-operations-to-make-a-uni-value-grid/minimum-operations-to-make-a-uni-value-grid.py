class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Median
        all_elements = []
        for row in grid:
            for num in row:
                all_elements.append(num)
        
        all_elements.sort()
        median = all_elements[len(all_elements) // 2]
        answer = 0
        for num in all_elements:
            difference = abs(median - num)
            if difference % x != 0:
                return -1
            answer += difference // x
        return answer