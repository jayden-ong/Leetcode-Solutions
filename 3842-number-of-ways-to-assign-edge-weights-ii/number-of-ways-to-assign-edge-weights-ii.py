class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = pow(10, 9) + 7
        num_nodes = len(edges) + 1
        curr, powers_of_two = 1, [1]
        for i in range(1, len(edges)):
            curr = 2 * curr % MOD
            powers_of_two.append(curr)

        parents = [-1] * (num_nodes + 1)
        depths = [0] * (num_nodes + 1)
        edges_dict = defaultdict(list)
        for start, end in edges:
            edges_dict[start].append(end)
            edges_dict[end].append(start)
        queue = deque([(1, 0)])
        visited = set()
        while queue:
            curr_node, curr_depth = queue.popleft()
            visited.add(curr_node)
            for next_node in edges_dict[curr_node]:
                if next_node not in visited:
                    queue.append((next_node, curr_depth + 1))
                    parents[next_node], depths[next_node] = curr_node, curr_depth + 1

        ancestors = [[0] * (num_nodes + 1) for _ in range(int(math.log(num_nodes - 1) / math.log(2)) + 1)]
        def build_ancestors():
            for i in range(len(ancestors[0])):
                ancestors[0][i] = parents[i]
            
            for i in range(1, len(ancestors)):
                for j in range(1, len(ancestors[0])):
                    ancestors[i][j] = ancestors[i - 1][ancestors[i - 1][j]]
        build_ancestors()

        def get_distance(node1, node2):
            if depths[node1] > depths[node2]:
                lca = get_lca(node1, node2)
            else:
                lca = get_lca(node2, node1)
            
            return depths[node1] + depths[node2] - 2 * depths[lca]

        def get_lca(node1, node2):
            diff = depths[node1] - depths[node2]
            mask, index = 1, 0
            while mask <= diff:
                if (mask & diff) > 0:
                    node1 = ancestors[index][node1]

                mask <<= 1
                index += 1

            if node1 == node2:
                return node1

            max_jumps = len(ancestors) - 1
            while max_jumps >= 0:
                if ancestors[max_jumps][node1] != ancestors[max_jumps][node2]:
                    node1, node2 = ancestors[max_jumps][node1], ancestors[max_jumps][node2]
                max_jumps -= 1
            
            return ancestors[0][node1]

        answer = []
        for first, second in queries:
            distance = get_distance(first, second)
            if distance == 0:
                answer.append(0)
            else:
                answer.append(powers_of_two[distance - 1])
        return answer