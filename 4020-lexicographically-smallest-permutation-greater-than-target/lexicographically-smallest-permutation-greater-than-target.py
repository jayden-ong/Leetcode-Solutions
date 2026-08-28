class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        chars = [0] * 26
        for char in s:
            chars[ord(char) - ord("a")] += 1

        def make_decision(curr_index, curr_answer):
            if curr_index == len(target):
                if curr_answer > target:
                    return curr_answer
                return ""
            
            target_char = target[curr_index]
            for i in range(26):
                if chars[i] > 0 and curr_answer + chr(i + ord('a')) >= target[:curr_index + 1]:
                    chars[i] -= 1
                    possible_answer = make_decision(curr_index + 1, curr_answer + chr(i + ord('a')))
                    if possible_answer != "":
                        return possible_answer
                    chars[i] += 1
            return ""
            
        return make_decision(0, "")