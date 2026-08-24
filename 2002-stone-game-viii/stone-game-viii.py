class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix_sum = []
        curr = 0
        for stone in stones:
            curr += stone
            prefix_sum.append(curr)
        
        f = [0] * n
        f[n - 1] = prefix_sum[n - 1]
        for i in range(n - 2, 0, -1):
            f[i] = max(f[i + 1], prefix_sum[i] - f[i + 1])
        return f[1]