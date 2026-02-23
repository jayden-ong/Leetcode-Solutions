class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes_found = set()
        for i in range(len(s) - k + 1):
            codes_found.add(s[i:i + k])
        return len(codes_found) == 2 ** k