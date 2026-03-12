class UnionFind:
        def __init__(self, size):
            self.parent = []
            for i in range(size):
                self.parent.append(i)
        
        def find_rep(self, curr_node):
            if self.parent[curr_node] == curr_node:
                return curr_node
            return self.find_rep(self.parent[curr_node])
        
        def union(self, node1, node2):
            rep1 = self.find_rep(node1)
            rep2 = self.find_rep(node2)
            self.parent[rep2] = rep1

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # Must contain n - 1 edges
        # All edges with must == 1, must be included in the spanning tree
        # If an edge is required, put both nodes in the same group
        edges_by_strength = []
        dsu = UnionFind(n)
        answer = float('inf')
        edges_added = 0
        for node1, node2, strength, required in edges:
            if required:
                # If they have the same rep, we have an unnecessary edge
                if dsu.find_rep(node1) == dsu.find_rep(node2):
                    return -1
                dsu.union(node1, node2)
                answer = min(answer, strength)
                edges_added += 1
            else:
                edges_by_strength.append((strength, node1, node2))
        edges_by_strength.sort(reverse=True)

        if edges_added == n - 1:
            return answer
        # We want to figure out when we can start boosting
        # We can add n - 1 - edges_added more edges
        #   We want to boost the edges with the samllest strength first
        #   Start boosting when k == n - 1 - edges_added
        start_boosting = k >= n - 1 - edges_added

        # We have already added all of the required edges
        # The goal is to greedily add all necessary edges and giving them a boost 
        for strength, node1, node2 in edges_by_strength:
            if dsu.find_rep(node1) != dsu.find_rep(node2):
                dsu.union(node1, node2)
                edges_added += 1
                if start_boosting:
                    answer = min(answer, 2 * strength)
                else:
                    start_boosting = k >= n - 1 - edges_added
                    answer = min(answer, strength)
                
                if edges_added == n - 1:
                    return answer
        return -1
        