class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # One option is all 1s
        nums_dict = defaultdict(int)
        answer = 0
        for num in nums:
            nums_dict[num] += 1
            if num == 1:
                answer += 1
        
        if answer % 2 == 0:
            answer -= 1
        answer = max(answer, 1)
        
        nums.sort()
        visited = set()
        for num in nums:
            if nums_dict[num] >= 2 and num not in visited and num != 1 and num != 1:
                curr, curr_answer = num ** 2, 1
                visited.add(num)
                visited.add(curr)
                while nums_dict[curr] >= 1:
                    curr_answer += 2
                    if nums_dict[curr] == 1:
                        break
                    curr **= 2
                    visited.add(curr)
                answer = max(answer, curr_answer)
        return answer