class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        string_n = format(n, "b")
        length_n = len(string_n)
        for i in range(1, length_n):
            if string_n[i - 1] == string_n[i]:
                return False
        return True