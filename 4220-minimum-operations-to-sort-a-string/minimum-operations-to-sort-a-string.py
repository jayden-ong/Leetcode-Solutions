class Solution:
    def minOperations(self, s: str) -> int:
        is_sorted = True
        min_char, max_char = min(s), max(s)
        sorted_in_two = False
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                is_sorted = False
            
            if 1 <= i < len(s) - 1 and (s[i] == min_char or s[i] == max_char):
                sorted_in_two = True
        
        if is_sorted:
            return 0
        
        if len(s) == 2:
            return -1
        
        if s[0] == min(s) or s[-1] == max(s):
            return 1
        
        if sorted_in_two:
            return 2
            
        return 3