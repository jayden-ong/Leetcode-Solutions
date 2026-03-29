class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # index 2 can only switch with index 0
        if not ((s1[0] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[2] and s1[2] == s2[0])):
            return False
        
        if not ((s1[1] == s2[1] and s1[3] == s2[3]) or (s1[1] == s2[3] and s1[3] == s2[1])):
            return False
        return True