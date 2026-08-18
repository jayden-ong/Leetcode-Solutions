class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        
        if k == len(nums):
            return max(nums)
        elif k == 1:
            answer = -1
            for num in nums_dict:
                if nums_dict[num] == 1:
                    answer = max(answer, num)
            return answer
        
        possible_answers = [-1]
        if nums_dict[nums[0]] == 1:
            possible_answers.append(nums[0])
        
        if nums_dict[nums[-1]] == 1:
            possible_answers.append(nums[-1])
        
        return max(possible_answers)