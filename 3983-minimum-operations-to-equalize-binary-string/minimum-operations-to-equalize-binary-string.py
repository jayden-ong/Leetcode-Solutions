class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # If k is even, the difference between 0 and 1 every time we perform an action will be even
        #   If you have 2 0s and 2 1s and k = 2, you can only affect the number of 0s and 1s by an even amount
        # If k is odd, you can affect each quantity by an odd amount
        nodes = [SortedList(range(0, len(s) + 1, 2)), SortedList(range(1, len(s) + 1, 2))]
        num_zeros = 0
        for char in s:
            if char == "0":
                num_zeros += 1
        
        queue = deque()
        queue.append(num_zeros)
        # Already have its solution
        nodes[num_zeros % 2].remove(num_zeros)
        distances = [float('inf')] * (len(s) + 1)
        distances[num_zeros] = 0
        while queue:
            curr_zeros = queue.popleft()
            upper, lower = curr_zeros + k - 2 * max(0, k - len(s) + curr_zeros), curr_zeros + k - 2 * min(curr_zeros, k)
            curr_set = nodes[lower % 2]
            index = curr_set.bisect_left(lower)
            while index < len(curr_set) and curr_set[index] <= upper:
                new_node = curr_set[index]
                distances[new_node] = distances[curr_zeros] + 1
                queue.append(new_node)
                curr_set.pop(index)
        
        if distances[0] == float('inf'):
            return -1
        return distances[0]