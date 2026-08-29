from collections import deque
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_dict = defaultdict(list)
        for i in range(len(nums) - 1, -1, -1):
            nums_dict[nums[i]].append(i)
        
        nums.sort()
        curr_nums = [nums[0]]
        curr_indices = [nums_dict[nums[0]][-1]]
        nums_dict[nums[0]].pop()
        answer = [0] * len(nums)
        for i in range(1, len(nums) + 1):
            # Have to add to list
            if i == len(nums) or nums[i] - curr_nums[-1] > limit:
                for num in curr_nums:
                    curr_index = heapq.heappop(curr_indices)
                    answer[curr_index] = num
                
                if i < len(nums):
                    curr_nums = [nums[i]]
                    curr_indices = [nums_dict[nums[i]][-1]]
                    nums_dict[nums[i]].pop()
            else:
                curr_nums.append(nums[i])
                heapq.heappush(curr_indices, nums_dict[nums[i]][-1])
                nums_dict[nums[i]].pop()
        return answer