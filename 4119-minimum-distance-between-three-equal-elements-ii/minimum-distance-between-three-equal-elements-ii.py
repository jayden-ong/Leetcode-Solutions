class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        nums_dict = defaultdict(list)
        answer = float('inf')
        for i, num in enumerate(nums):
            nums_dict[num].append(i)
            if len(nums_dict[num]) >= 3:
                last_index = len(nums_dict[num]) - 1
                answer = min(answer, abs(nums_dict[num][last_index] - nums_dict[num][last_index - 1]) + abs(nums_dict[num][last_index - 1] - nums_dict[num][last_index - 2]) + abs(nums_dict[num][last_index] - nums_dict[num][last_index - 2]))

        if answer == float('inf'):
            return -1
        return answer