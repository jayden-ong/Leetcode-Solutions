class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        edges_dict = defaultdict(list)
        for start, end, distance in roads:
            edges_dict[start].append((end, distance))
            edges_dict[end].append((start, distance))
        # find all edges in the component that connects nodes 1 and n
        queue = deque()
        queue.append(1)
        visited = set()
        visited.add(1)
        answer = float('inf')
        while queue:
            curr_node = queue.popleft()
            for dest, distance in edges_dict[curr_node]:
                if dest not in visited:
                    queue.append(dest)
                    visited.add(dest)
        
        for start, end, distance in roads:
            if start in visited or end in visited:
                answer = min(answer, distance)
        return answer