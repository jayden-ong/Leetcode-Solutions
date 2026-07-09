class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        prefix_sum = []
        for i in range(len(nums)):
            if i == 0:
                prefix_sum.append(1)
            elif nums[i] - nums[i - 1] <= maxDiff:
                prefix_sum.append(prefix_sum[-1] + 1)
            else:
                prefix_sum.append(prefix_sum[-1])
        
        answer = []
        for left, right in queries:
            if prefix_sum[right] - prefix_sum[left] == right - left:
                answer.append(True)
            else:
                answer.append(False)
        return answer

