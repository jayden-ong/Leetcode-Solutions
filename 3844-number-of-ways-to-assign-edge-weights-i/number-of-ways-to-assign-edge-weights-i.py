class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7
        edges_dict = defaultdict(list)
        for start, end in edges:
            edges_dict[start].append(end)
            edges_dict[end].append(start)
        
        node_queue = deque()
        node_queue.append((1, 0))
        visited = set()
        max_depth = 0
        while node_queue:
            curr_node, curr_distance = node_queue.popleft()
            max_depth = max(max_depth, curr_distance)
            visited.add(curr_node)
            for destination in edges_dict[curr_node]:
                if destination not in visited:
                    node_queue.append((destination, curr_distance + 1))
        
        return 2 ** (max_depth - 1) % MOD