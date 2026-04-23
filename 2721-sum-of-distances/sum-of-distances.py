class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num_to_index = defaultdict(list)
        for i, num in enumerate(nums):
            num_to_index[num].append(i)
        
        answer = [0] * len(nums)
        for num in num_to_index:
            for i, index in enumerate(num_to_index[num]):
                if i == 0:
                    answer[index] = sum(num_to_index[num]) - num_to_index[num][0] * len(num_to_index[num])
                else:
                    answer[index] = answer[num_to_index[num][i - 1]] - (len(num_to_index[num]) - i - 1) * (num_to_index[num][i] - num_to_index[num][i - 1]) + (i - 1) * (num_to_index[num][i] - num_to_index[num][i - 1])
        return answer