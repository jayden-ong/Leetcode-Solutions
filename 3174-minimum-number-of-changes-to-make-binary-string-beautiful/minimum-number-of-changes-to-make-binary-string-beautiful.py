class Solution:
    def minChanges(self, s: str) -> int:
        num_char = 1
        curr_char = s[0]
        freq_list = []
        for i in range(1, len(s) + 1):
            if i == len(s) or curr_char != s[i]:
                freq_list.append(num_char)
                num_char = 1
                if i < len(s):
                    curr_char = s[i]
            else:
                num_char += 1
        
        seen_odd = False
        answer = 0
        for num in freq_list:
            if num % 2 == 0:
                if seen_odd:
                    answer += 1
            else:
                if seen_odd:
                    answer += 1
                    seen_odd = False
                else:
                    seen_odd = True
        return answer


            