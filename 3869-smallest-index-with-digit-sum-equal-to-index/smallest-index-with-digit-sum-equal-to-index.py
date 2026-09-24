class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def calculate_digit_sum(num):
            answer = 0
            for digit in str(num):
                answer += int(digit)
            return answer
        
        for i, num in enumerate(nums):
            if calculate_digit_sum(num) == i:
                return i
        return -1

            
