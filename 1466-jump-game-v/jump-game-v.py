class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        jump_lengths = [[max(0, i - d), min(len(arr) - 1, i + d)] for i in range(len(arr))]
        indices_heap = []
        for i, num in enumerate(arr):
            indices_heap.append((num, i))
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    jump_lengths[i][0] = j + 1
                    break
                
            for j in range(i + 1, min(len(arr), i + d + 1)):
                if arr[j] >= arr[i]:
                    jump_lengths[i][1] = j - 1
                    break

        dp = [1] * len(arr)
        heapq.heapify(indices_heap)
        while indices_heap:
            _, i = heapq.heappop(indices_heap)
            for jump_point in range(jump_lengths[i][0], jump_lengths[i][1] + 1):
                if jump_point != i:
                    dp[i] = max(dp[i], dp[jump_point] + 1)
        return max(dp)
