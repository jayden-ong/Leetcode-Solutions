class Solution:
    def minOperations(self, s: str) -> int:
        length_s = len(s)
        if length_s % 2 == 0:
            answer1 = "01" * (length_s // 2)
            answer2 = "10" * (length_s // 2)
        else:
            answer1 = "01" * (length_s // 2) + "0"
            answer2 = "10" * (length_s // 2) + "1"
        
        changes1 = 0
        changes2 = 0
        for i in range(length_s):
            if answer1[i] != s[i]:
                changes1 += 1
            
            if answer2[i] != s[i]:
                changes2 += 1
        return min(changes1, changes2)