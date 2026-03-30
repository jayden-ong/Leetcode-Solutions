class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd_chars = defaultdict(int)
        even_chars = defaultdict(int)
        for i in range(len(s1)):
            if i % 2 == 0:
                even_chars[s1[i]] += 1
            else:
                odd_chars[s1[i]] += 1
        
        for i in range(len(s1)):
            if i % 2 == 0:
                if even_chars[s2[i]] > 0:
                    even_chars[s2[i]] -= 1
                else:
                    return False
            else:
                if odd_chars[s2[i]] > 0:
                    odd_chars[s2[i]] -= 1
                else:
                    return False
        return True