class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        answer = 0
        answer_set = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                if i == j:
                    continue
                for k in range(len(digits)):
                    if i == k or j == k:
                        continue
                    
                    curr = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if curr % 2 == 0 and digits[i] != 0 and curr not in answer_set:
                        answer += 1
                        answer_set.add(curr)
        return answer