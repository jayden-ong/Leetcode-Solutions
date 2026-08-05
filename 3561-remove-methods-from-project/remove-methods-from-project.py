class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        edges_dict = defaultdict(list)
        for start, end in invocations:
            edges_dict[start].append(end)
        
        queue = deque()
        queue.append(k)
        visited = set()
        while queue:
            curr_node = queue.popleft()
            visited.add(curr_node)
            for dest in edges_dict[curr_node]:
                if dest not in visited:
                    queue.append(dest)
        
        answer = []
        if len(visited) == n:
            return answer
        
        for i in range(n):
            if i not in visited:
                for dest in edges_dict[i]:
                    if dest in visited:
                        return [i for i in range(n)]
            
                answer.append(i)

        return answer