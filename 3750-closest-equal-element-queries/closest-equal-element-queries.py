class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums_dict = defaultdict(list)
        num_index_to_index = {}
        for i, num in enumerate(nums):
            nums_dict[num].append(i)
            num_index_to_index[(num, i)] = len(nums_dict[num]) - 1

        answer = []
        for query in queries:
            target = nums[query]
            if len(nums_dict[target]) <= 1:
                answer.append(-1)
                continue
            
            index_in_nums_dict = num_index_to_index[(target, query)]
            if index_in_nums_dict == 0:
                answer.append(min(abs(query - nums_dict[target][-1] + len(nums)), abs(query - nums_dict[target][index_in_nums_dict + 1])))
            elif index_in_nums_dict == len(nums_dict[target]) - 1:
                answer.append(min(abs(query - nums_dict[target][index_in_nums_dict - 1]), abs(query - nums_dict[target][0] - len(nums))))
            else:
                answer.append(min(abs(query - nums_dict[target][index_in_nums_dict - 1]), abs(query - nums_dict[target][index_in_nums_dict + 1])))
            
        return answer