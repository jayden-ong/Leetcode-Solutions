class Solution:
    def minJumps(self, arr: List[int]) -> int:
        val_to_index = defaultdict(list)
        for i, num in enumerate(arr):
            val_to_index[num].append(i)
        
        queue = deque()
        queue.append((0, 0))
        visited = set()
        visited.add(0)
        while queue:
            i, num_steps = queue.popleft()
            if i == len(arr) - 1:
                return num_steps

            if i - 1 >= 0 and i - 1 not in visited:
                queue.append((i - 1, num_steps + 1))
                visited.add(i - 1)
            
            if i + 1 < len(arr) and i + 1 not in visited:
                queue.append((i + 1, num_steps + 1))
                visited.add(i + 1)
            
            for new_index in val_to_index[arr[i]]:
                if new_index != i and new_index not in visited:
                    queue.append((new_index, num_steps + 1))
                    visited.add(new_index)
            val_to_index[arr[i]] = []
        # Should never run
        return -1