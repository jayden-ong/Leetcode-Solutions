class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        index_used = set()
        queue = deque()
        queue.append(start)
        index_used.add(start)
        while queue:
            curr = queue.popleft()
            if arr[curr] == 0:
                return True
            
            if curr - arr[curr] >= 0 and curr - arr[curr] not in index_used:
                index_used.add(curr - arr[curr])
                queue.append(curr - arr[curr])
            
            if curr + arr[curr] < len(arr) and curr + arr[curr] not in index_used:
                index_used.add(curr + arr[curr])
                queue.append(curr + arr[curr])

        return False