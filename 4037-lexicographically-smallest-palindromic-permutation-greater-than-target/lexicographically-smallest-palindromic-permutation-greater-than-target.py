class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        chars = [0] * 26
        num_odd = 0
        for char in s:
            chars[ord(char) - ord('a')] += 1
            if chars[ord(char) - ord('a')] % 2 == 1:
                num_odd += 1
            else:
                num_odd -= 1
        
        if num_odd > 1:
            return ""
        
        def make_decision(curr_index, curr_answer):
            if (curr_index == len(target) // 2 and len(target) % 2 == 0) or (curr_index == len(target) // 2 + 1 and len(target) % 2 == 1):
                if ''.join(curr_answer) > target:
                    return ''.join(curr_answer)
                return ""
            for i in range(26):
                if ''.join(curr_answer[:curr_index]) + chr(i + ord('a')) >= target[:curr_index + 1] and (chars[i] >= 2 or (chars[i] == 1 and curr_index == len(target) // 2)):
                    curr_answer[curr_index] = curr_answer[len(curr_answer) - 1 - curr_index] = chr(i + ord('a'))
                    chars[i] -= 2
                    possible_answer = make_decision(curr_index + 1, curr_answer)
                    if possible_answer != "":
                        return possible_answer
                    chars[i] += 2
                    curr_answer[curr_index] = curr_answer[len(curr_answer) - 1 - curr_index] = ''
            return ""
        return make_decision(0, [''] * len(target))