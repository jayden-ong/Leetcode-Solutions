class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        def find_longest_prefix(string_num1, string_num2, best_answer):
            for i in range(min(len(string_num1), len(string_num2)), best_answer, -1):
                if string_num1[:i] == string_num2[:i]:
                    return i
            # Means there is nothing better than best_answer
            return -1
        
        answer = 0
        for num1 in arr1:
            for num2 in arr2:
                string_num1 = str(num1)
                string_num2 = str(num2)
                if min(len(string_num1), len(string_num2)) > answer and string_num1[:answer] == string_num2[:answer]:
                    answer = max(answer, find_longest_prefix(string_num1, string_num2, answer))
        return answer
        '''
        all_prefixes = set()
        for num in arr1:
            curr = ""
            for char in str(num):
                curr += char
                all_prefixes.add(curr)
        
        answer = 0
        for num in arr2:
            str_num = str(num)
            for i in range(len(str_num), answer, -1):
                if str_num[:i] in all_prefixes:
                    answer = i
                    break
        return answer