class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        curr_start = 1
        answer = []
        while curr_start <= 9:
            curr = curr_start
            next_num = curr + 1
            while next_num <= 10:
                if low <= curr <= high:
                    answer.append(curr)
                
                if curr > high:
                    break
                
                curr = curr * 10 + next_num
                next_num += 1
            curr_start += 1
        answer.sort()
        return answer