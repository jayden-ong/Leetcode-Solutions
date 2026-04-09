class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7
        buckets = [[] for _ in range(int(len(nums) ** 0.5))]
        for left, right, k, multiply in queries:
            if k < int(len(nums) ** 0.5):
                buckets[k].append((left, right, multiply))
            else:
                for i in range(left, right + 1, k):
                    nums[i] = nums[i] * multiply % MOD
        
        difference = [1] * (len(nums) + int(len(nums) ** 0.5))
        for k in range(1, int(len(nums) ** 0.5)):
            if not buckets[k]:
                continue
            difference[:] = [1] * len(difference)
            for left, right, multiply in buckets[k]:
                difference[left] = difference[left] * multiply % MOD
                next_right = ((right - left) // k + 1) * k + left
                difference[next_right] = difference[next_right] * pow(multiply, MOD - 2, MOD) % MOD
            for i in range(k, len(nums)):
                difference[i] = difference[i] * difference[i - k] % MOD
            for i in range(len(nums)):
                nums[i] = nums[i] * difference[i] % MOD
        
        answer = nums[0]
        for i in range(1, len(nums)):
            answer ^= nums[i]
        return answer